# Analysis receipt

A one-page record that travels with any qualitative or AI-assisted analysis. It says what the analysis read, what it left over, whether anyone checked the leftovers, and what each claim rests on.

> Every AI analysis makes compromises. Document yours.

## Start here, no code needed

| | |
|---|---|
| **[Read the guide (web page)](https://sashamitts.github.io/analysis-receipt/)** | What the receipt is, how to fill it in, and a filled example. The easiest place to start. |
| **[Make your own copy (Google Doc)](https://docs.google.com/document/d/1lnpzzmbP78J6_D8i5rWgcrJrw0qvGXN5vC1y7F1eo0I/copy)** | The blank receipt, ready to fill in. Download it as Word from Google Docs if you prefer. |
| **[Download the printable PDF](print/analysis-receipt.pdf)** | A one-page quick guide, the blank receipt, and a filled example. |

The rest of this repository holds the same receipt in plain text, add-on sections for other study designs, detailed guides, a leftover sampler script and a Claude skill.

## Why

AI tools now summarise interviews, cluster survey responses and draft findings in minutes. Their output often looks complete and checks out line by line. What it leaves out is invisible in the output itself. A tool may have read a sample, cut long documents, or dropped what few people said. The people reading the report cannot see any of that. People leave things out too, and the same record helps there.

The receipt makes those choices visible. It does not certify an analysis. It shows what the analysis rests on, and what it did not look at.

## What is in this repository

| Folder | What it holds |
|---|---|
| [`receipt/`](receipt/) | The blank receipt, a one-table compact version, and optional modules for different study designs |
| [`guide/`](guide/) | How to adapt it to your study, how to fill each line, and what it can and cannot show |
| [`examples/`](examples/) | A real filled receipt from the Learners East 2026 demonstration, and two invented examples for other study designs |
| [`tools/`](tools/) | `leftover_sample.py`, which finds the passages no finding used, draws a random sample for a person to read, and computes the bound |
| [`prompts/`](prompts/) | Reader briefs for targeted searches with AI or people |
| [`skill/`](skill/) | A Claude skill that helps you adapt, fill in and review a receipt |
| [`print/`](print/) | The printable PDF (quick guide, blank receipt, filled example) and its source pages |
| [`docs/`](docs/) | The web page at sashamitts.github.io/analysis-receipt |

## Start here

1. **Read [`guide/ADAPTING.md`](guide/ADAPTING.md)** (10 minutes). Research comes in many shapes. The receipt keeps four parts fixed and lets you change the rest. The guide walks through five decisions that fit it to your study.
2. **Copy [`receipt/analysis-receipt.md`](receipt/analysis-receipt.md)** next to your analysis, add the [modules](receipt/modules.md) your study needs, and fill it in **while you work**. A record made afterwards is a memory, and memories leave things out too.
3. **Run the leftover check** (line 3.2). It is the one line that produces new evidence.
4. **Attach the [compact version](receipt/analysis-receipt-compact.md)** to the report or readout, and link the full receipt.

## The four parts

| Part | Lines | Owner |
|---|---|---|
| **Question** | Question and frame. What it means for the decision. | Whoever set the question |
| **Readers** | What was collected. What was read, and by which readers. What was never read. | Whoever ran the reading |
| **Leftovers** | What counts as a leftover. What was sampled, and what it found. Targeted searches. What was not checked. | Whoever checks what was set aside |
| **Claims** | What each claim rests on, with the cases against it. Claims that did not hold. | Whoever reports the findings |

One person can own all four. In a team they are often different people, and each signs their part.

## The leftover check

A **leftover** is a passage (a turn, a response, a note) that no finding used. Nobody can read every leftover. A person can read a random sample.

```bash
python3 tools/leftover_sample.py split  --docs transcripts.csv --speaker "User:" --out passages.csv
python3 tools/leftover_sample.py sample --passages passages.csv --findings findings.json --n 60 --seed 2026
# label each sampled passage: existing / new / nothing
python3 tools/leftover_sample.py tally  --sample leftover_sample.csv
```

If 60 random leftovers hold nothing new, the share of leftovers holding a new idea is probably under 5% (95% confidence). That bounds how much is left. It does **not** find rare ideas, which one or two people voiced and which usually fall outside any random sample. For those, add a targeted search ([`prompts/reader-briefs.md`](prompts/reader-briefs.md)). See [`guide/LIMITS.md`](guide/LIMITS.md).

The script uses only the Python standard library. Run `python3 tools/leftover_sample.py --help` for input formats.

## The Claude skill

The skill in [`skill/analysis-receipt/`](skill/analysis-receipt/) helps you:

- **adapt** the receipt to how your study ran,
- **fill** it from your materials, without inventing numbers,
- **run** the leftover check, and
- **review** a receipt for vague or missing entries.

To install it:

- **Claude apps (claude.ai, desktop):** download [`skill/analysis-receipt.zip`](skill/analysis-receipt.zip) and upload it in Claude's settings where custom skills are managed. Skills must be available on your plan and enabled for your organisation. Anthropic's help centre has the current steps.
- **Claude Code:** copy the `skill/analysis-receipt/` folder into `~/.claude/skills/` (for you) or `.claude/skills/` in a project (for a team).

Then ask, for example, "Help me adapt the analysis receipt for my diary study", or "Review this receipt".

If you change files in `receipt/`, `guide/`, `prompts/` or `tools/`, run `tools/build_skill.sh` to copy them into the skill and rebuild the zip.

## Adapting and contributing

The receipt is a baseline for common approaches, not a standard. If a line does not fit your work, change it and say why. If you write a module others could use, or find that the four parts do not fit your kind of research, please open an issue or a pull request.

## Background

The receipt borrows from reporting practice in other fields: PRISMA flow diagrams in systematic reviews, which report what was excluded and why; auditing standards, which require reasons when evidence could not be obtained; and proposed audit cards for AI evaluations, which ask what was left out of scope. It was introduced in the talk "Finding What AI Analysis Misses" at Learners East 2026. Sources are in [`guide/LIMITS.md`](guide/LIMITS.md).

## Citing

See [`CITATION.cff`](CITATION.cff). Suggested: Mitts, S. (2026). *Analysis receipt* [Template and tools]. GitHub.

## License

- Template, guides, examples and prompts: [CC BY 4.0](LICENSE-CC-BY-4.0.md). Reuse and adapt with credit.
- Code (`tools/`) and the skill's instructions (`skill/analysis-receipt/SKILL.md` and `scripts/`): [MIT](LICENSE-MIT). The reference files copied into the skill keep their CC BY 4.0 license.
