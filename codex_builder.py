import argparse
import json
from pathlib import Path

from ritual_utils import list_scrolls, first_line


def build_codex():
    codex = []
    for file in list_scrolls():
        codex.append({
            'file': file.name,
            'first_line': first_line(file),
        })
    return codex


def main() -> None:
    parser = argparse.ArgumentParser(
        description='Build JSON codex from ritual files'
    )
    parser.add_argument(
        '--write', action='store_true', help='Write codex.json to disk'
    )
    args = parser.parse_args()

    codex = build_codex()

    if args.write:
        Path('codex.json').write_text(
            json.dumps(codex, indent=2), encoding='utf-8'
        )
        print('codex.json written.')
    else:
        print(json.dumps(codex, indent=2))


if __name__ == '__main__':
    main()
