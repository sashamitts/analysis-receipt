# Analysis receipt: Learners East 2026 demonstration

A real, filled receipt. It describes the demonstration in the talk "Finding What AI Analysis Misses" (Learners East, 9 October 2026). The study is small and was run to illustrate the method, so read the numbers as an example, not as a finding about AI tools in general.

**Study or project:** How several ways of reading the same interviews differ in what they find
**Analysis owner:** Sasha Mitts
**Date range of the analysis:** 1 to 8 October 2026
**Receipt version:** v1

---

## 1. Question

### 1.1 Question and frame
"How do these professionals decide what to hand to AI, what to keep for themselves, and when to check its work?"
Given word for word to every AI reader. The human reference reader read for the same question. No theoretical framework was applied. Out of scope by design: anything not about handing work over, keeping it, or checking it, although several participants talked about their jobs more widely.

### 1.2 What it means for the decision
A demonstration for a talk. No product or policy decision rests on it.

---

## 2. Readers

### 2.1 What was collected
12 interviews drawn at random (seed 20261009) from the 1,000 workforce interviews in the public Anthropic Interviewer dataset. 16,963 words in total. 138 participant turns.

### 2.2 What was read, and by which readers

| Reader | Person, model or tool | What it was given | What it actually read | Instructions or brief |
|---|---|---|---|---|
| R | Sasha Mitts, blind, before seeing any AI output | All 12 transcripts | All 12, turn by turn | The question only |
| A | claude-sonnet-5-5, effort high, 8 Oct 2026 | All 12 in one prompt | All 12 (well inside the context limit) | "Identify the key themes" |
| A×4 | The same model and prompt, 3 more runs | As A | As A | As A |
| B | gpt-6.1-sol and muse-spark-1.3, effort high, 8 Oct 2026 | As A | As A | As A |
| C | claude-sonnet-5-5, 4 separate calls | As A | As A | Four briefs: every distinct answer; where the question does not fit; specific episodes; say versus do |

Output cap 32,000 tokens per call. No call hit it. Exact prompts, model IDs and settings are in the run log.

How the material reached each model. Each call received all 12 interviews in one prompt, in the same order every time. Nothing was chunked or retrieved. This suits patterns across people. It may cost detail within each person, and any effect of the order was the same in every call. Temperature was not set, so each provider's default applied.

### 2.3 What was never read, and why
Nothing in the 12 interviews was skipped. The other 988 interviews were not drawn.

---

## 3. Leftovers

### 3.1 What counts as a leftover here
Unit is a participant turn. A turn is a leftover if no AI finding quotes it. 45 of the 138 turns were leftovers.

### 3.2 What was sampled, and what it found

| Total leftovers | Sampled | Seed | Read by | Existing finding | New idea | Nothing relevant | Upper bound on the share holding a new idea (95%) |
|---|---|---|---|---|---|---|---|
| 45 | 20 | 20261009-leftovers | Sasha Mitts | 8 | 0 | 12 (11 greetings or sign-offs) | 14% |

3 of the 8 belonged to an idea no AI reader had found (worry about being displaced).

### 3.3 Targeted searches for rare or misfitting material
Reader C's four briefs. The "where the question does not fit" brief found one participant whose admin work was not theirs to hand over. The human reading had already noted it.

### 3.4 What was not checked
The 988 interviews not drawn. One human reference reader and no second adjudicator. Reading one interview per call, or shuffling the order between calls, was not tested. Claude proposed the matches between AI findings and the reference ideas; Sasha checked 20 of them at random, and all 20 held.

---

## 4. Claims

### 4.1 What each claim rests on

| Claim | Supporting records | Cases against it | What the cases against it showed | Checked by |
|---|---|---|---|---|
| One model in one pass found 19 of the 34 ideas in the human reading (56%) | 34 ideas grouped from 135 human findings; each AI link checked | Not applicable | | Sasha, 20 random links |
| All AI readers together found 27 of 34 (79%) | As above | | | |
| Every idea held by five or more people was found; all 7 misses were held by four or fewer | Idea by participant grid from the human reading | | | Computed by code |

All 526 quotes in the AI findings were found word for word in the transcripts (checked by code).

### 4.2 Claims that did not hold
The AI readers proposed 3 ideas the human reading lacked. Checked against the transcripts:
- People's stated trust or rules differ from what they describe doing. Partly held. Of the cases checked, most dissolved on a close reading.
- Some judgement outputs get no independent check. Partly held. The interview did not ask about checking directly.
- For some people there is no real handover decision. Held, but was already in the human reading.

---

## Sign-off

| Line | Owner | Signed |
|---|---|---|
| 1. Question | Sasha Mitts | |
| 2. Readers | Sasha Mitts | |
| 3. Leftovers | Sasha Mitts | |
| 4. Claims | Sasha Mitts | |
