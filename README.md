# Prompt Engine

A comic prompt generator with preset system and UI/CLI tools.

## Overview

Prompt Engine is a tool for comic creators to generate structured AI image prompts. It features a React-based UI for selecting character presets, editing fields, and managing prompts, plus a Python CLI for batch processing.

## Quick Start

### CLI (Prototype 1)

```bash
cd prototype_1
python prompt_generator.py --json example_prompts.json
```

With presets (resolves `presetId` references):

```bash
python prompt_generator.py --json test_with_presets.json --presets presets.json
```

### UI (Prototype 2)

```bash
cd prototype_2/ui
python -m http.server 8000
```

Open http://localhost:8000 in your browser.

## Features

- **Character Presets**: Define reusable character types (Neko Deer, Neko Rabbit, etc.).
- **Preset Dropdowns**: Search and select presets in the UI; fields auto-populate.
- **Merge/Overwrite**: Apply presets with merge (preserve edits) or overwrite modes.
- **Edited Indicator**: Badge shows when fields differ from the preset.
- **Persistence**: Presets auto-save to localStorage in the UI.
- **Import/Export**: Export/import presets as JSON files.
- **Preset Manager**: CRUD interface to create, edit, and delete presets.
- **CLI Preset Resolution**: `presetId` references are resolved at assembly time.
- **Live Prompt Preview**: Real-time prompt text updates as you edit.
- **Copy to Clipboard**: Quick export of assembled prompts.

## Project Structure

```
prototype_1/
  ├── prompt_generator.py     # CLI with preset resolution
  ├── example_prompts.json    # Full example (explicit fields)
  ├── test_with_presets.json  # Example using presetId references
  ├── presets.json            # Character preset definitions
  ├── brainstorm_1.md         # Project vision
  └── README.md               # Usage guide

prototype_2/
  ├── prompt_generator.py     # Same CLI as prototype_1
  ├── presets.json            # Presets
  ├── test_with_presets.json  # Test with presetId
  ├── README.md               # CLI & UI usage
  ├── aims.md                 # Prototype 2 goals & success criteria
  └── ui/
      ├── index.html          # React entry point
      ├── app.js              # Main app component + Preset Manager
      ├── styles.css          # Styling
      ├── presets.json        # Bundled presets for UI
      └── README.md           # UI setup instructions
```

## Data Format

### Prompt JSON (with presetId)

```json
{
  "scene": "2 girls, yoga studio with cameras and floodlights,",
  "characters": [
    {
      "name": "Character 1",
      "age": 21,
      "presetId": "neko_deer_01",
      "details": "sweating slightly, blushing slightly"
    },
    {
      "name": "Character 2",
      "age": 23,
      "presetId": "neko_rabbit_01"
    }
  ],
  "interactions": "character 2's arms around character 1's shoulders, ...",
  "camera": "8k, ultra realism, perfect composition, masterful colour balance"
}
```

### Preset Schema

```json
{
  "schemaVersion": "1.0",
  "presets": [
    {
      "id": "neko_deer_01",
      "name": "Neko Deer (Shy)",
      "tags": ["neko", "deer", "shy"],
      "appearance": "humanoid Neko deer girl, blue eyes, ...",
      "default_expression": "smiling nervously, biting lip",
      "default_position": "arms crossed, shy posture",
      "default_actions": "making peace sign",
      "description": "A timid deer-neko with soft brown tones."
    }
  ]
}
```

## How It Works

1. **Define Presets**: Create character presets in `presets.json` with default appearance, expression, position, and actions.
2. **Build Prompts**: In the UI, select presets for each character; fields auto-populate.
3. **Edit & Customize**: Modify any field; edited fields are marked and preserved.
4. **Export**: Export prompts as JSON (with `presetId` references) or copy raw text.
5. **CLI Assembly**: Run `prompt_generator.py` with exported JSON; missing fields are resolved from presets.

## Safety & Compliance

- All characters must have an `age` field (≥18).
- No automatic enforcement; responsibility on user to ensure proper content.

## Next Steps

- [ ] Scaffold production React/Vite project.
- [ ] Add expression/position/action preset dropdowns.
- [ ] Implement character avatar/thumbnail previews.
- [ ] Export variants for Midjourney, Stable Diffusion, etc.
- [ ] Cloud preset sync and user authentication.

## License

MIT
