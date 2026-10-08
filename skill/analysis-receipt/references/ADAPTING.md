# Adapting the receipt to your study

Research is not one shape. The receipt is a baseline with four parts that hold across most qualitative analysis, whether it is done by people, by AI tools, or by both. The details under each part should change with your study. This guide shows how to make those changes deliberately.

## What stays fixed

Four questions sit under every version of the receipt. Keep them, even if you rename the lines.

1. **Question.** What was asked, and what decision it serves.
2. **Readers.** What was read, by whom or by what, and what was never read.
3. **Leftovers.** What was set aside, and whether anyone checked it.
4. **Claims.** What each finding rests on, and the cases against it.

Each part has an owner, a person who can be asked about it. One person can own all four. In a team, they are often different people.

## What you will need to decide

Work through these five decisions before you start, and write the answers into the receipt. They take about 15 minutes for a typical study.

### 1. What is a passage?

The leftover check needs a unit. Pick the smallest unit that can carry one idea on its own.

- Interviews: one participant turn is a good default. Very long turns can be split at paragraph breaks.
- Survey open-ends: one response.
- Usability sessions: one task attempt, or one timestamped observation.
- Field notes: one dated entry, or one paragraph.
- Documents and literature: one section, or one paragraph.

### 2. What makes a passage a leftover?

Common definitions, from strictest to loosest:

- No finding quotes it.
- No finding quotes or cites it.
- No code was applied to it.

Choose the one you can compute. If your tool shows which passages it used, use that. If it only gives quotes, match quotes back to passages (the sampler script does this).

### 3. Who or what counts as a reader?

Anything that turns material into findings is a reader: a person coding, a model summarising, a search step that decides what a model sees. If a tool has hidden steps, list the tool as one reader and say what you cannot see.

### 4. How big a leftover sample?

The sample bounds how much was missed. It does not find rare things. Rough guide:

| Sample with nothing new | Upper bound on the share of leftovers with a new idea (95%) |
|---|---|
| 20 | about 14% |
| 30 | about 10% |
| 60 | about 5% |
| 100 | about 3% |

Pick the bound you can live with for the decision at hand. A design exploration may accept 15%. A policy recommendation may need 5% or less. Run `python3 tools/leftover_sample.py bound` for other numbers.

### 5. Which targeted search fits the risk?

Random samples miss what one or two people said. If rare views matter for the decision, add at least one targeted search and record it under 3.3. The briefs in `prompts/reader-briefs.md` are starting points.

## Common approaches

These are starting points, not rules. Your study may combine several.

| Approach | Passage | Leftover | Readers to list | Modules to consider |
|---|---|---|---|---|
| Interviews, thematic analysis by one researcher with an AI summary | Participant turn | Turn no finding quotes | The researcher; the AI tool with version; any transcription service | AI tools in the reading |
| Interviews, team coding with a codebook | Turn or coded segment | Segment with no code | Each coder; the codebook version | Several human coders; Codebook development |
| Survey open-ends, AI clustering | One response | Response not in any cluster summary | The clustering tool; whoever named the clusters | Survey open-ends; AI tools in the reading |
| Usability study, notes and recordings | Task attempt or timestamped note | Observation not in the findings | Note taker; whoever watched recordings; any AI summariser | Usability sessions |
| Diary study | One entry | Entry no finding cites | Readers per wave | Longitudinal |
| Literature or desk review | Section or paragraph of a source | Source section not cited | Screeners; any AI search or summary tool | Synthesis across studies |
| Automated research pipeline | Whatever the pipeline chunks by | Chunk no output cites | Each pipeline stage | Fully automated pipelines |

## When a line does not fit

- **The line does not apply.** Keep it and write "Not applicable" with one reason. A missing line reads as "not checked".
- **The line applies but you cannot answer it.** Write what you know and what you cannot see. "The tool does not show which documents it read" is a valid entry, and an important one.
- **You need a line the receipt does not have.** Add a module (see `receipt/modules.md`, and "Writing your own module" at its end).
- **The four parts do not fit your work at all.** Tell us how in an issue. That is useful for the next version.

## Adopting it in a team

- Start with one study, and fill the receipt during the work rather than at the end. A record made afterwards is a memory, and memories leave things out too.
- Attach the compact receipt to every readout that uses AI analysis. Keep the full one where reviewers can find it.
- Use the same lines every time, so people learn where to look.
- Treat the receipt as an account the owners sign, not as a checklist to tick. Checklists can turn into ritual. The leftover sample and the claim checks are what keep it from becoming one, because they produce new evidence.
