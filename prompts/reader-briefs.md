# Reader briefs

Different readers find different things. One model asked once for "the key themes" tends to report what many people said, and to drop what few people said. A reader given a specific target finds more of that target. These briefs split the reading by what to look for, not by persona.

Use them with a model, or give them to people. Run each brief as a separate call or a separate reader, so one brief does not crowd out another. Record each one on the receipt under 2.2 (who read, with which brief) and 3.3 (targeted searches).

They were written for interviews. Change the nouns for your material (responses, sessions, entries, sources). Keep the task sentence specific.

## Shared header

```
You are helping analyse research [interviews].

Research question: {QUESTION}

Below are {N} [interview transcripts]. Each begins with its [participant] ID. Read all of them.
```

## Baseline: themes

The usual single-pass request. Run it so you have something to compare the others with.

```
Identify the key themes that answer the research question.
```

## Brief 1: every distinct answer

Targets answers that only one or two people give.

```
List every distinct answer participants give to the research question, one per finding,
including answers only one participant gives. Tag each answer with every participant who gives it.
```

## Brief 2: where the question does not fit

Targets the question nobody asked: people for whom the premise does not hold.

```
Find participants for whom the assumptions behind the research question do not hold.
For example, they do not face this choice, someone or something else makes it for them,
or they frame the matter in other terms. Quote them and state which assumption fails.
```

## Brief 3: specific episodes

Targets concrete events, which carry conditions and turning points that general statements smooth over.

```
Find specific events participants recount that bear on the research question, such as a time
something went wrong or went well. Report what happened and what the participant did differently
afterwards. Events only, not general statements. Include a quote for the "afterwards".
```

## Brief 4: what people say and what they describe doing

Targets differences within one person, which only show when two passages are read together.

```
Find places where a participant's general statement about the research question differs from
something else they say or describe doing in the same interview. Quote both passages and state
the difference in one sentence. Context-dependent behaviour is not inconsistency; report only
real differences.
```

Expect many of these to dissolve on a close reading. In our demonstration, none of the say-do gaps a model proposed held in full when checked against the transcripts. Check each one before reporting it, and log the ones that did not hold under 4.2.

## Output format

Asking for verbatim quotes lets you check them by code, and tells you which passages each reader used, which you need for the leftover check.

```
Return JSON only, with no other text: a list of objects, one per finding, each with these fields.
- "finding": the finding, in one sentence.
- "participants": the IDs of every participant who supports it, as a list.
- "quotes": verbatim quotes that support it, as a list of {"participant": ID, "text": the exact words}.
  Copy the words exactly. Do not paraphrase inside a quote.
- "departs_from": for findings about a broken assumption or a gap between what someone says and does,
  name the assumption or statement it departs from in one sentence. Otherwise use an empty string.
```

## Writing your own brief

A good brief names one thing to find, says what counts and what does not, and asks for evidence that can be checked. Split briefs by kinds of thing you could miss in your study: a group, a condition, a stage of a process, a kind of event. Persona briefs ("read as a skeptic") have shown little gain in the studies we know of.
