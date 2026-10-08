#!/usr/bin/env python3
"""
Leftover sampling for the analysis receipt (lines 3.1 and 3.2).

Standard library only. Python 3.8 or later.

WHAT IT DOES
  split   Turn transcripts (one row per document) into passages (one row per turn or paragraph).
  sample  Find the passages no finding used (the leftovers) and draw a seeded random sample to read.
  tally   Count the labels you gave the sample and report the upper bound for the receipt.
  bound   Compute the upper bound directly, for planning a sample size.

THE IDEA IN ONE PARAGRAPH
  A "leftover" is a passage that no finding quoted or cited. Nobody can read all of them, but a
  person can read a random sample. If a random sample of n leftovers holds k new ideas, we can put
  an upper bound on the share of all leftovers that hold one. With k = 0 and n = 60 the bound is
  about 5% (95% confidence). The bound says how much is probably left. It does not find rare ideas,
  which usually fall outside any random sample; use a targeted search for those (receipt line 3.3).

QUICK START
  python3 leftover_sample.py split  --docs transcripts.csv --id-col id --text-col text \
                                    --speaker "User:" --out passages.csv
  python3 leftover_sample.py sample --passages passages.csv --findings findings.json \
                                    --n 60 --seed 2026 --out leftover_sample.csv
  # read leftover_sample.csv and fill the "label" column: existing / new / nothing
  python3 leftover_sample.py tally  --sample leftover_sample.csv
  python3 leftover_sample.py bound  --n 60 --found 0

INPUT FORMATS
  passages.csv   columns: passage_id, source, text
                 (source is the document or participant the passage came from)
  findings       either
                   a JSON list of findings, each with "quotes": [{"participant" or "source": ID, "text": "..."}]
                   a CSV with columns text and (optionally) source, one quote per row
                   a CSV with a passage_id column, listing passages that were used directly
"""
import argparse
import csv
import json
import random
import re
import sys
from collections import Counter
from pathlib import Path

csv.field_size_limit(10**9)


# ---------- helpers ----------------------------------------------------------

def norm(s):
    """Lower-case, straighten curly quotes, drop punctuation, collapse spaces.
    Lets a quote match its passage even if a curly quote or double space changed.
    Anything bigger than that (a changed word) will not match, on purpose."""
    s = (s or "").lower()
    s = s.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')
    s = re.sub(r"[^\w\s']", " ", s)
    return re.sub(r"\s+", " ", s).strip()


def read_csv(path):
    with open(path, newline="", encoding="utf-8-sig") as fh:
        return list(csv.DictReader(fh))


def write_csv(path, rows, fields):
    with open(path, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=fields)
        w.writeheader()
        for r in rows:
            w.writerow({k: r.get(k, "") for k in fields})


def binom_cdf(k, n, p):
    """P(X <= k) for X ~ Binomial(n, p)."""
    total, term = 0.0, (1 - p) ** n
    for i in range(0, k + 1):
        if i > 0:
            term *= (n - i + 1) / i * p / (1 - p) if p < 1 else 0.0
        total += term
    return total


def upper_bound(found, n, conf=0.95):
    """One-sided exact (Clopper-Pearson) upper bound on the true rate,
    given `found` hits in `n` random draws. Found by bisection on the binomial CDF."""
    if n <= 0:
        raise ValueError("sample size must be positive")
    if found >= n:
        return 1.0
    alpha = 1 - conf
    lo, hi = found / n, 1.0
    for _ in range(100):
        mid = (lo + hi) / 2
        if binom_cdf(found, n, mid) > alpha:
            lo = mid
        else:
            hi = mid
    return hi


# ---------- split -------------------------------------------------------------

def cmd_split(a):
    """One row per document in, one row per passage out.
    With --speaker, a passage is one turn by that speaker (lines starting with the prefix,
    plus following lines until another speaker starts). Without it, passages are paragraphs."""
    others = [o.strip() for o in (a.other_speakers or "").split(",") if o.strip()]
    out = []
    for doc in read_csv(a.docs):
        src, text = doc[a.id_col], doc[a.text_col] or ""
        chunks = []
        if a.speaker:
            cur = None
            for line in text.splitlines():
                if line.startswith(a.speaker):
                    if cur is not None:
                        chunks.append(cur)
                    cur = line[len(a.speaker):].strip()
                elif any(line.startswith(o) for o in others):
                    if cur is not None:
                        chunks.append(cur)
                    cur = None
                elif cur is not None:
                    cur += " " + line.strip()
            if cur is not None:
                chunks.append(cur)
        else:
            chunks = [p.strip() for p in re.split(r"\n\s*\n", text) if p.strip()]
        for k, c in enumerate(chunks, start=1):
            if len(c.split()) >= a.min_words:
                out.append({"passage_id": f"{src}#T{k}", "source": src, "text": c})
    write_csv(a.out, out, ["passage_id", "source", "text"])
    print(f"Wrote {len(out)} passages from {len(set(r['source'] for r in out))} documents to {a.out}")


# ---------- sample ------------------------------------------------------------

def load_used(path):
    """Return (used passage ids, list of (source or None, normalised quote))."""
    p = Path(path)
    ids, quotes = set(), []
    if p.suffix.lower() == ".json":
        data = json.loads(p.read_text(encoding="utf-8"))
        items = data if isinstance(data, list) else next((v for v in data.values() if isinstance(v, list)), [])
        for f in items:
            for q in f.get("quotes", []) or []:
                if isinstance(q, str):
                    quotes.append((None, norm(q)))
                else:
                    quotes.append((q.get("participant") or q.get("source"), norm(q.get("text", ""))))
            for pid in f.get("passage_ids", []) or []:
                ids.add(pid)
    else:
        for r in read_csv(path):
            if r.get("passage_id"):
                ids.add(r["passage_id"])
            elif r.get("text"):
                quotes.append((r.get("source") or None, norm(r["text"])))
    return ids, [q for q in quotes if q[1]]


def cmd_sample(a):
    passages = read_csv(a.passages)
    used_ids = set()
    quotes = []
    for f in a.findings:
        i, q = load_used(f)
        used_ids |= i
        quotes += q
    leftovers, matched_quotes = [], set()
    for p in passages:
        nt = norm(p["text"])
        hit = p["passage_id"] in used_ids
        for j, (src, q) in enumerate(quotes):
            if (src is None or src == p["source"]) and q in nt:
                hit = True
                matched_quotes.add(j)
        if not hit:
            leftovers.append(p)
    unmatched = len(quotes) - len(matched_quotes)
    rng = random.Random(a.seed)
    pick = rng.sample(leftovers, min(a.n, len(leftovers)))
    for r in pick:
        r["label"], r["note"] = "", ""
    write_csv(a.out, pick, ["passage_id", "source", "text", "label", "note"])
    print(f"Passages: {len(passages)}")
    print(f"Used by findings: {len(passages) - len(leftovers)}")
    print(f"Leftovers: {len(leftovers)}")
    print(f"Sampled: {len(pick)} (seed {a.seed}) -> {a.out}")
    if quotes:
        print(f"Quotes that matched no passage: {unmatched} of {len(quotes)}"
              " (changed quotes, or quotes from outside the passages; worth a look)")
    print("Next: label each sampled passage as existing, new or nothing, then run tally.")


# ---------- tally and bound ---------------------------------------------------

def cmd_tally(a):
    rows = read_csv(a.sample)
    labels = Counter((r.get("label") or "").strip().lower() for r in rows)
    n = len(rows)
    new = sum(c for l, c in labels.items() if l.startswith("new"))
    blank = labels.get("", 0)
    print(f"Sample size: {n}")
    for l, c in sorted(labels.items(), key=lambda x: -x[1]):
        print(f"  {l or '(blank)'}: {c}")
    if blank:
        print(f"Warning: {blank} rows have no label. The bound below treats them as read.")
    ub = upper_bound(new, n, a.conf)
    print(f"New ideas found: {new} of {n}")
    print(f"Upper bound on the share of leftovers holding a new idea ({int(a.conf * 100)}%): {ub:.1%}")
    print("For the receipt, line 3.2: total leftovers, sample size, seed, who read it, the counts above, and the bound.")


def cmd_bound(a):
    ub = upper_bound(a.found, a.n, a.conf)
    print(f"{a.found} found in {a.n} random draws -> upper bound {ub:.1%} at {int(a.conf * 100)}% (one-sided, exact)")
    if a.found == 0:
        print(f"Rule-of-three approximation: {3 / a.n:.1%}")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)

    s = sub.add_parser("split", help="split documents into passages")
    s.add_argument("--docs", required=True, help="CSV with one document per row")
    s.add_argument("--id-col", default="id")
    s.add_argument("--text-col", default="text")
    s.add_argument("--speaker", help='prefix of the participant\'s lines, for example "User:" or "P:"')
    s.add_argument("--other-speakers", default="", help='comma-separated prefixes of other speakers, for example "AI:,Interviewer:"')
    s.add_argument("--min-words", type=int, default=1, help="drop passages shorter than this")
    s.add_argument("--out", default="passages.csv")
    s.set_defaults(func=cmd_split)

    s = sub.add_parser("sample", help="find leftovers and draw a random sample")
    s.add_argument("--passages", required=True)
    s.add_argument("--findings", required=True, nargs="+", help="one or more JSON or CSV files")
    s.add_argument("--n", type=int, default=60)
    s.add_argument("--seed", required=True, help="write it on the receipt")
    s.add_argument("--out", default="leftover_sample.csv")
    s.set_defaults(func=cmd_sample)

    s = sub.add_parser("tally", help="count labels and report the bound")
    s.add_argument("--sample", required=True)
    s.add_argument("--conf", type=float, default=0.95)
    s.set_defaults(func=cmd_tally)

    s = sub.add_parser("bound", help="compute an upper bound")
    s.add_argument("--n", type=int, required=True)
    s.add_argument("--found", type=int, default=0)
    s.add_argument("--conf", type=float, default=0.95)
    s.set_defaults(func=cmd_bound)

    a = ap.parse_args()
    a.func(a)


if __name__ == "__main__":
    main()
