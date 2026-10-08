# Optional modules

The core receipt has four parts and nine lines. Most studies need a few more. Pick the modules that match how your study actually ran, and add them under the part they belong to. Delete the rest. Do not keep a module only because it is here.

Each module says which part it extends and what to write.

---

## AI tools in the reading

**Extends:** 2.2 What was read

Add one row per model or AI feature, even when it is built into a larger tool (a transcription service, a research repository, a "summarise" button).

- Model and version, provider, and the date it ran. Models change without notice, so the date matters.
- Settings that change output, if you can see them: reasoning effort, temperature, output length cap.
- How the material reached the model: the whole text, chunks, search results, or a sample. If the tool decides this for you, say so and say what you know about it.
- Context or file limits you hit, and what happened to material past the limit.
- Whether you can see what it read. If not, write "The tool does not show what it read."
- Where the prompts or briefs are kept.

## Several human coders

**Extends:** 2.2 What was read, and 4.1 Claims

- Who coded what, and whether independently.
- How disagreements were settled, and by whom.
- Agreement statistics, if you report them, with a note that agreement is measured on what was coded. It says nothing about what nobody coded.

## Codebook development

**Extends:** 1.1 Question and frame, and 3 Leftovers

- Whether the codebook was set in advance, built from the data, or both.
- Version and date of the codebook used for the final pass.
- Codes added from the leftover sample or targeted searches, and the passages that prompted them.

## Survey open-ends and other short responses at scale

**Extends:** 2.1 What was collected, and 3.1 What counts as a leftover

- The unit is usually one response. Very short responses ("n/a", "fine") may be excluded from leftovers; say how many and by what rule.
- If responses were deduplicated or clustered before reading, say how, and how many were represented by another response rather than read.
- Weighting, if findings are reported as shares of a population.

## Usability sessions, field notes and observation

**Extends:** 2.1 What was collected, and 3.1 What counts as a leftover

- What the record is: recordings, transcripts, notes, screenshots, logs. Readers often see only one of these.
- Whether non-verbal material (screens, behaviour, tone) was read or only the transcript. Transcripts drop most of what happens on screen.
- The unit for leftovers, for example a task attempt or a timestamped note.

## Longitudinal, diary and repeated contact

**Extends:** 2.2 What was read, and 4.1 Claims

- Which waves or entries each reader saw. Readers given one wave cannot see change over time.
- Whether claims about change were checked against each person's earlier entries.

## Synthesis across studies, desk research and literature

**Extends:** 2.1 What was collected, and 2.3 What was never read

- Search sources, terms and dates. Inclusion and exclusion rules, with counts at each step (PRISMA style).
- Studies retrieved but not read in full, and why.
- Whether earlier syntheses were reused, and what they in turn left out, if known.

## Mixed methods

**Extends:** 4.1 Claims

- Which claims rest on qualitative material, which on numbers, and which on both.
- Where the two disagreed, and what was done about it.

## Sensitive topics, consent and exclusions

**Extends:** 2.3 What was never read

- Material excluded for consent, safety or legal reasons, as counts. Do not describe the content.
- Whether exclusions fall unevenly across groups, which can bias findings.

## Recontact and member checking

**Extends:** 3.3 Targeted searches, and 4.2 Claims that did not hold

- Who was recontacted, about which claims, and what changed.

## Fully automated pipelines

**Extends:** 2.2 What was read, and 3 Leftovers

- The pipeline version and a link to its configuration.
- Log of what reached each model, compared with each document's length. A log of calls is a more reliable record than a model's own account of what it skipped.
- Who read the leftover sample. If nobody did, the receipt should say "Leftovers not sampled".

---

## Writing your own module

Write a module when a step in your study changes what gets read or what counts as a finding. Give it:

1. A name.
2. The part it extends.
3. Two to five prompts that ask for counts, names, versions or reasons, not adjectives.

If you write one others could use, consider opening a pull request.
