Prompt Generator CLI

Usage

- Basic usage (no presets):

```bash
python prompt_generator.py --json example_prompts.json
```

- With presets (resolves `presetId` fields):

```bash
python prompt_generator.py --json test_with_presets.json --presets presets.json
```

Files

- `prompt_generator.py`: CLI that assembles prompts and resolves preset IDs.
- `example_prompts.json`: Full prompt example (all fields explicit).
- `test_with_presets.json`: Example using `presetId` references (compact).
- `presets.json`: Reusable character presets.

Notes

- Characters can use `presetId` to reference a preset; missing fields are filled from the preset.
- Each character should include an `age` field (>=18).
- Use `--presets` to specify a custom presets file (defaults to `presets.json`).