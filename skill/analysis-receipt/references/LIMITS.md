# What the receipt can and cannot do

## It is not a certificate

A filled receipt does not mean an analysis is good. It means someone can see what the analysis rests on, and what it did not look at. Weak work with an honest receipt is easier to judge than strong-looking work without one.

## The leftover sample bounds common misses. It does not find rare ones.

If a random sample of 60 leftovers holds nothing new, the share of leftovers carrying a new idea is probably under 5%. That is a bound, not a guarantee that nothing is left. An idea one or two people voiced, in a handful of passages among hundreds, will usually fall outside any random sample of 60. Rare views need a targeted search (line 3.3).

The arithmetic: with zero hits in n random draws, the one-sided 95% upper bound on the hit rate is 1 − 0.05^(1/n), close to 3/n (the "rule of three"). With some hits, the script uses the exact binomial (Clopper-Pearson) bound.

## The reference is never ground truth

Any comparison of readers needs a reference, usually a careful human reading. That reader misses things too. When another reader finds something the reference lacks, check it against the records before counting it either way.

## Agreement is not coverage

Two readers can agree closely on the passages they both coded and still miss the same things. Agreement statistics are computed on what was put in front of the readers. They cannot see what nobody found.

## Self-reports about what was skipped are unreliable

This holds for models and people. Models often do not mention the factors that shaped their answers, and people are poor reporters of their own reasoning. That is why the receipt asks for records made during the work, such as a log of what reached each model, rather than an account written afterwards.

## Checklists can become ritual

A receipt filled in after the fact, by someone who did not do the work, records very little. The two lines that resist this are the leftover sample and the claim checks, because each produces new evidence. If those two are blank, the rest of the receipt is description only.

## Sources

- Hanley, J. A., and Lippman-Hand, A. (1983). If nothing goes wrong, is everything all right? *JAMA*, 249(13). The rule of three.
- Page, M. J., et al. (2021). The PRISMA 2020 statement. *BMJ*, 372, n71. Reporting what was excluded, and why.
- International Standard on Auditing 705 (Revised), paragraph 24. Auditors state the reasons when evidence could not be obtained.
- Staufer, L., Yang, M., Reuel, A., and Casper, S. (2025). Audit cards. arXiv:2504.13839. Preprint. Asks evaluators to state what was excluded from scope.
- Russell, D. M., Stefik, M. J., Pirolli, P., and Card, S. K. (1993). The cost structure of sensemaking. *INTERCHI '93*. Residue: data that does not fit the current schema.
- Morse, J. M., et al. (2002). Verification strategies for establishing reliability and validity in qualitative research. *International Journal of Qualitative Methods*, 1(2). A critique of audit trails that record decisions without testing them.
- Barbour, R. S. (2001). Checklists for improving rigour in qualitative research. *BMJ*, 322. The risk of checklists as ritual.
- Turpin, M., et al. (2023). Language models don't always say what they think. *NeurIPS*. Model explanations omit factors that shaped the answer.
- Nisbett, R. E., and Wilson, T. D. (1977). Telling more than we can know. *Psychological Review*, 84(3). People's reports of their own reasoning.
