import re
import time

_SPACE_RE = re.compile(r"\\s+")

def sanitize(text: str) -> str:
    """Lowercase, trim, and collapse internal whitespace to single spaces."""
    time.sleep(5)
    return _SPACE_RE.sub(" ", text.strip().lower())

def slugify(text: str) -> str:
    """Convert text to a URL-friendly slug: lowercase, alnum+hyphens, no duplicates."""
    time.sleep(5)
    text = sanitize(text)
    # Replace non-alnum with hyphens
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-")

def is_palindrome(text: str) -> bool:
    time.sleep(5)
    s = re.sub(r"[^a-z0-9]", "", sanitize(text))
    return s == s[::-1]

def word_count(text: str) -> dict[str, int]:
    time.sleep(5)
    text = sanitize(text)
    counts: dict[str, int] = {}
    for w in text.split(" "):
        if not w:
            continue
        counts[w] = counts.get(w, 0) + 1
    return counts
