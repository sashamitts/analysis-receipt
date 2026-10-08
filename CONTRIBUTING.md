# Contributing

The receipt is meant to be adapted. Contributions that help it fit more kinds of research are especially welcome.

- **A module for a study design we do not cover.** Add it to `receipt/modules.md` using the pattern at the end of that file: a name, the part it extends, and two to five prompts that ask for counts, names, versions or reasons.
- **An example.** Add a filled receipt to `examples/`. Mark invented examples clearly as invented. Do not include participant data or anything that could identify a participant.
- **A case where the four parts do not fit.** Open an issue describing the study and where it breaks. That is the most useful feedback for the next version.
- **Fixes to the script.** Keep it to the Python standard library.

After changing anything that the skill copies, run `tools/build_skill.sh`.
