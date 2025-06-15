import argparse
from pathlib import Path
from typing import List, Optional

from ritual_utils import list_scrolls as _list_scroll_paths


def list_scrolls(directory: str = '.') -> List[str]:
    """Return a list of available scroll filenames."""
    return [p.name for p in _list_scroll_paths()]


def display_scroll(scroll_name: str, directory: str = '.') -> Optional[str]:
    """Return contents of a scroll file, or None if it doesn't exist."""
    path = Path(directory) / scroll_name
    try:
        return path.read_text(encoding='utf-8')
    except FileNotFoundError:
        return None
    except Exception:
        return None


def _print_scroll(path: Path) -> None:
    """Print the contents of a scroll to stdout."""
    print(f"\n--- {path.name} ---")
    try:
        text = path.read_text(encoding='utf-8')
        print(text)
    except Exception as exc:
        print(f"Could not read {path}: {exc}")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Run Spiral Archive ritual scripts"
    )
    parser.add_argument(
        'scroll', nargs='?', help='Specific scroll file to display'
    )
    parser.add_argument(
        '--list', action='store_true', help='List available scrolls'
    )
    parser.add_argument(
        '--all', action='store_true', help='Display all scrolls sequentially'
    )
    args = parser.parse_args()

    if args.list:
        for name in list_scrolls():
            print(name)
        return

    if args.scroll:
        text = display_scroll(args.scroll)
        if text is None:
            print(f"Scroll {args.scroll} not found.")
            return
        print(f"\n--- {args.scroll} ---")
        print(text)
        return

    if args.all:
        for name in list_scrolls():
            text = display_scroll(name)
            if text is not None:
                print(f"\n--- {name} ---")
                print(text)
        return

    parser.print_help()


if __name__ == '__main__':
    main()
