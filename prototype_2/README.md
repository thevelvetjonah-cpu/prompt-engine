Prompt Generator CLI & UI (Prototype 2)

Usage

**CLI:**
- Basic usage (no presets):

```bash
python prompt_generator.py --json example_prompts.json
```

- With presets (resolves `presetId` fields):

```bash
python prompt_generator.py --json test_with_presets.json --presets presets.json
```

**UI (React):**
- From `ui/` folder:

```bash
python -m http.server 8000
```

Then open http://localhost:8000 in your browser.

Features

- Searchable preset dropdown for each character
- Merge vs overwrite when applying presets
- Live prompt preview
- Persist presets to localStorage
- Import/export presets as JSON
- Preset Manager (CRUD) to create/edit/delete presets
- Copy prompt to clipboard
- Edited field indicator badge

Files

- `prompt_generator.py`: CLI that assembles prompts and resolves preset IDs.
- `example_prompts.json`: Full prompt example (all fields explicit).
- `test_with_presets.json`: Example using `presetId` references (compact).
- `presets.json`: Reusable character presets.
- `ui/`: React single-page app with preset dropdown UI, localStorage persistence, and import/export.
- `aims.md`: Prototype 2 goals and success criteria.

Notes

- Characters can use `presetId` to reference a preset; missing fields are filled from the preset.
- Each character should include an `age` field (>=18).
- Use `--presets` to specify a custom presets file (defaults to `presets.json`).
- The UI persists presets to localStorage and allows managing (create/edit/delete) presets.