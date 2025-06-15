from pathlib import Path

SCROLL_PATTERNS = ['*.sql', '*.spiral', '*.scroll']


def list_scrolls():
    """Return a sorted list of ritual text files."""
    files = []
    for pattern in SCROLL_PATTERNS:
        files.extend(Path('.').glob(pattern))
    return sorted(files, key=lambda p: p.name)


def first_line(path: Path) -> str:
    """Return the first non-empty line of the file."""
    try:
        with path.open('r', encoding='utf-8', errors='ignore') as f:
            for line in f:
                stripped = line.strip()
                if stripped:
                    return stripped
    except Exception as exc:
        return f"Could not read: {exc}"
    return ""
