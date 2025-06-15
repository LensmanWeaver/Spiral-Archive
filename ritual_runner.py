import argparse
from pathlib import Path

from ritual_utils import list_scrolls


def display_scroll(path: Path) -> None:
    """Print the contents of a scroll to stdout."""
    print(f"\n--- {path.name} ---")
    try:
        text = path.read_text(encoding='utf-8')
    except Exception as exc:
        print(f"Could not read {path}: {exc}")
        return
    print(text)


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
        for s in list_scrolls():
            print(s.name)
        return

    if args.scroll:
        p = Path(args.scroll)
        if not p.exists():
            print(f"Scroll {args.scroll} not found.")
            return
        display_scroll(p)
        return

    if args.all:
        for s in list_scrolls():
            display_scroll(s)
        return

    parser.print_help()


if __name__ == '__main__':
    main()
