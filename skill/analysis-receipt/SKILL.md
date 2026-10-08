---
name: analysis-receipt
description: Help a researcher adapt, fill in, or review an analysis receipt, the one-page record of what a qualitative or AI-assisted analysis read, left over, sampled and rests on. Use when someone mentions an analysis receipt, wants to document what an AI analysis did not read, or wants to check what a synthesis may have missed.
---

# Analysis receipt

An analysis receipt is a short record that travels with an analysis. It has four parts, each owned by a person who can be asked about it:

1. **Question.** The question and frame, and what the analysis means for the decision.
2. **Readers.** What was collected, what each reader (person, model or tool) actually read, and what was never read.
3. **Leftovers.** What no finding used, a random sample of it read by a person, targeted searches for rare material, and what was not checked.
4. **Claims.** What each claim rests on, the cases against it, and claims that did not hold.

The full template is in `references/analysis-receipt.md`. Optional lines for other study designs are in `references/modules.md`.

Your job is to help the person produce an honest, specific receipt for **their** study. Studies differ a great deal. Never force their work into the shape of the examples.

## Work out what they need

Ask, or infer from what they gave you, which of these they want. Often it is more than one, in this order.

- **Adapt.** Make a version of the receipt that fits how their study ran.
- **Fill.** Fill in the receipt from their materials and answers.
- **Sample.** Help them run the leftover check (line 3.2).
- **Review.** Check a receipt they already wrote.
- **Compact.** Produce the one-table version for a report or slide (`references/analysis-receipt-compact.md`).

## Adapt

Read `references/ADAPTING.md` before starting. Then settle five things with the person. Ask in one short batch, offer a sensible default for each, and let them answer only what they know.

1. The shape of the study: method, material, how many sources, who and what did the reading.
2. What a **passage** is in their material (turn, response, note, task attempt, entry, section).
3. What makes a passage a **leftover** (no finding quotes it; no finding cites it; no code applied). Choose a definition they can actually compute.
4. Who or what counts as a **reader**. Include tool features that summarise, cluster, retrieve or transcribe.
5. How much uncertainty the decision can tolerate, which sets the sample size (see the table in ADAPTING.md).

Then propose: the core lines, the modules from `references/modules.md` that fit, and any custom line their study needs. For each module you add, say in one line why. Leave out modules that do not fit. Keep every core line; if one does not apply, it stays with "Not applicable" and a reason.

## Fill

Read `references/FILLING.md` for what strong entries look like.

- **Counts, names, versions, dates and reasons.** Not adjectives. "24 interviews; 4 over the tool's length limit" rather than "a good number of interviews".
- **Never invent a number, a model version, a seed or a result.** If you do not know it, write it as an open item: `Not known yet: <what is missing and who can supply it>`. A gap the person can see is better than a confident guess.
- **Ask for records, not recollections.** Prefer logs, exports, file counts and the tool's own documentation over anyone's memory of what happened. Do not take a model's own account of what it read or skipped as evidence. If you produced findings yourself earlier in the conversation, you are one of the readers. List yourself, and do not certify your own coverage.
- **What a tool actually read** is the line people most often get wrong. Ask how material reached each model (whole text, chunks, search results, a sample) and whether anything was cut. If they cannot tell, the entry is "The tool does not show what it read."
- **Owners sign, not you.** Leave the sign-off for the people named.

## Sample (the leftover check)

This is the one line that produces new evidence. Help them do it rather than describe it.

1. Agree the passage unit and leftover definition from Adapt.
2. If they can give you the material and the findings (with quotes or passage IDs), use `scripts/leftover_sample.py`:
   - `split` turns documents into passages,
   - `sample` finds the leftovers and draws a seeded random sample,
   - `tally` counts their labels and computes the upper bound,
   - `bound` gives the bound for any sample size, for planning.
   If you cannot run code, explain the steps so they can, or work out the bound from the table in ADAPTING.md.
3. **A person reads and labels the sample**: existing finding, new idea, or nothing relevant. Do not label the sample yourself unless they explicitly ask, and if they do, say on the receipt that a model labelled it.
4. Report the bound in plain words, for example: "No new ideas in 60 random leftovers, so the share of leftovers holding a new idea is probably under 5%." Always add that this does not find rare ideas, and suggest a targeted search (line 3.3, `references/reader-briefs.md`) if rare views matter for the decision.
5. If the sample finds new ideas, that is the check working. Help them add the idea to the findings and record it.

## Review

Check an existing receipt line by line. Report, briefly:

- Lines left blank, which read as "not checked". Ask for an entry or "Not applicable" with a reason.
- Entries with adjectives where a count, name or reason is needed.
- Missing denominators ("12 participants said X", of how many?).
- Readers whose actual reading is unstated, especially AI features.
- A leftover line with no sample, or a sample with no seed, size or reader.
- Claims with no cases against them stated, and no record of claims that were dropped.
- Places where the receipt claims more than its evidence shows.

Be direct and specific. Do not rewrite their receipt unless they ask; suggest the change.

## Tone and limits

- A receipt is not a certificate. Never describe a filled receipt as showing the analysis is complete, correct or unbiased. It shows what the analysis rests on and what it did not look at.
- Keep the person's own terms for their study, groups and findings.
- If the four parts truly do not fit their work, say so and help them write the closest honest record. Suggest they open an issue in the repository so the template can improve.

## Files

- `references/analysis-receipt.md`: full blank template
- `references/analysis-receipt-compact.md`: one-table version
- `references/modules.md`: optional lines by study design
- `references/ADAPTING.md`: the five decisions, and common approaches
- `references/FILLING.md`: weak and strong entries for each line
- `references/LIMITS.md`: what the receipt and the sample can and cannot show
- `references/reader-briefs.md`: briefs for targeted searches
- `references/example-learners-2026.md`: a real filled receipt
- `scripts/leftover_sample.py`: split, sample, tally and bound (standard library Python)
