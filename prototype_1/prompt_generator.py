import json
import argparse
import sys
import os


def load_presets(preset_path: str) -> dict:
    """Load presets from JSON file; return {preset_id -> preset object}."""
    try:
        if not os.path.exists(preset_path):
            return {}
        with open(preset_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        presets_list = data.get("presets", []) if isinstance(data, dict) else (data if isinstance(data, list) else [])
        return {p.get("id"): p for p in presets_list if p.get("id")}
    except Exception as e:
        print(f"Warning: failed to load presets from {preset_path}: {e}", file=sys.stderr)
        return {}


def resolve_character(ch: dict, presets: dict) -> dict:
    """Resolve a character by filling missing fields from preset if presetId is set."""
    preset_id = ch.get("presetId")
    if not preset_id or preset_id not in presets:
        return ch
    preset = presets[preset_id]
    resolved = dict(ch)
    if not resolved.get("appearance"):
        resolved["appearance"] = preset.get("appearance")
    if not resolved.get("expression"):
        resolved["expression"] = preset.get("default_expression")
    if not resolved.get("position"):
        resolved["position"] = preset.get("default_position")
    if not resolved.get("actions"):
        resolved["actions"] = preset.get("default_actions")
    return resolved


def assemble_prompt(data: dict, presets: dict = None) -> str:
    if presets is None:
        presets = {}
    parts = []
    scene = data.get("scene")
    if scene:
        parts.append(scene.rstrip(', '))

    characters = data.get("characters", [])
    for idx, ch in enumerate(characters, start=1):
        resolved_ch = resolve_character(ch, presets)
        name = resolved_ch.get("name", f"Character {idx}")
        seg = []
        if resolved_ch.get("appearance"):
            seg.append(f"{name} appearance = {resolved_ch['appearance']}")
        if resolved_ch.get("expression"):
            seg.append(f"{name} expression = {resolved_ch['expression']}")
        if resolved_ch.get("position"):
            seg.append(f"{name} position = {resolved_ch['position']}")
        if resolved_ch.get("actions"):
            seg.append(f"{name} actions = {resolved_ch['actions']}")
        if resolved_ch.get("details"):
            seg.append(f"{name} details = {resolved_ch['details']}")
        if seg:
            parts.append(", ".join(seg))

    if data.get("interactions"):
        parts.append(f"character interactions= {data['interactions']}")

    if data.get("camera"):
        parts.append(f"camera= {data['camera']}")

    return "\n\n".join(parts)


def main():
    parser = argparse.ArgumentParser(description="Prompt generator for comic creator.")
    parser.add_argument("--json", "-j", help="Path to prompt JSON file", required=True)
    parser.add_argument("--presets", "-p", help="Path to presets JSON file (optional)", default="presets.json")

    args = parser.parse_args()

    try:
        with open(args.json, "r", encoding="utf-8") as f:
            data = json.load(f)
    except Exception as e:
        print(f"Failed to read JSON: {e}")
        sys.exit(1)

    presets = load_presets(args.presets)
    prompt = assemble_prompt(data, presets)
    print(prompt)


if __name__ == "__main__":
    main()