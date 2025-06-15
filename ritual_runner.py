import os

SCROLL_EXTENSIONS = ('.sql', '.scroll', '.spiral')


def list_scrolls(directory: str = '.'):
    """Return a list of available scroll files in the given directory."""
    return [f for f in os.listdir(directory) if f.endswith(SCROLL_EXTENSIONS)]


def display_scroll(scroll_name: str, directory: str = '.'):
    """Return contents of a scroll file, or None if it doesn't exist."""
    path = os.path.join(directory, scroll_name)
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        return None
    except Exception:
        return None
