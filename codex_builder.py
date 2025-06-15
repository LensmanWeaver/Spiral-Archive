import argparse
import json
from pathlib import Path


def list_scroll_files():
    """Return sorted list of scroll-like files."""
    patterns = ['*.sql', '*.spiral', '*.scroll']
    files = []
    for pattern in patterns:
        files.extend(Path('.').glob(pattern))
    return sorted(files, key=lambda p: p.name)


def first_line(path: Path) -> str:
    """Return the first non-empty line of the file."""
    try:
        for line in path.read_text(encoding='utf-8', errors='ignore').splitlines():
            stripped = line.strip()
            if stripped:
                return stripped
    except Exception as exc:
        return f"Could not read: {exc}"
    return ""


def build_codex():
    codex = []
    for file in list_scroll_files():
        codex.append({
            'file': file.name,
            'first_line': first_line(file),
        })
    return codex


def main() -> None:
    parser = argparse.ArgumentParser(description='Build JSON codex from ritual files')
    parser.add_argument('--write', action='store_true', help='Write codex.json to disk')
    args = parser.parse_args()

    codex = build_codex()
    print(json.dumps(codex, indent=2))

    if args.write:
        Path('codex.json').write_text(json.dumps(codex, indent=2), encoding='utf-8')
        print('codex.json written.')


if __name__ == '__main__':
    main()
