Prototype 2 — Aims (Presets + Dropdown UI)

Goal:
- Add reusable character presets and a dropdown selector so users can choose animal types for each character slot and auto-fill fields.

Checklist / Roadmap:
- Create `presets.json` format and place in prototype folder.
- Load presets at app start and expose them to the editor.
- Add a searchable `PresetDropdown` in each `CharacterCard`.
- Selecting a preset populates (appearance, expression, position, actions).
- Support merge vs overwrite when applying presets.
- Show an "edited" indicator when user changes fields after applying a preset.
- Persist user presets (localStorage) and support import/export JSON.
- Ensure CLI export includes `presetId` if used.

Success criteria (Prototype 2):
- `presets.json` exists with at least 3 presets.
- UI (or prototype flow) can select a preset and populate character fields.
- User edits after applying a preset are preserved (fields editable).
- Exported JSON contains `presetId` and the final assembled prompt matches applied/edited fields.
- Presets can be exported/imported as JSON.

Notes:
- Keep the preset schema minimal and versioned for future upgrades.
- This prototype focuses on the UX flow; backing sync/server is out of scope for now.