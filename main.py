"""The Meeting That Should Have Been One Line.

Writes the single sentence that could have replaced an entire
pointless meeting to /output/entry.txt.
"""

import os

ENTRY = "Gary emailed all 14 of us at 7:12 that the deadline moved to Friday, so this meeting is just him reading his own email back to us."


def checked_entry(text):
    stripped = text.strip()
    if not stripped:
        raise ValueError("entry must not be blank")
    if len(stripped) > 200:
        raise ValueError("entry exceeds 200 characters")
    if "\n" in stripped or "\r" in stripped:
        raise ValueError("entry must be a single line")
    return stripped


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(checked_entry(ENTRY))


if __name__ == "__main__":
    main()
