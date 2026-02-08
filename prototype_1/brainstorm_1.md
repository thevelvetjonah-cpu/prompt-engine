Brainstorm 1 — summary

- Purpose: UI-first prompt generator for comic creators to build image prompts via scene + character presets.
- Key features: scene library, character presets, dropdowns for expressions/positions, interactions builder, live prompt preview, JSON export.
- Safety: app will require `age` fields in inputs; explicit moderation optional (not enforced in prototype).
- MVP: single-page editor, add 2 character presets, live preview, export JSON/plain prompt.
- Tech note: start with React + TypeScript; optional Electron wrap later.

Context: prototype includes CLI prompt assembler (`prompt_generator.py`) and an example JSON. Save these as a starting point for UI prototyping.