"""Entry for make.fun competition: u-kevin-the-funniest-office-joke-judged-head-to-head-3dc3233c.

Running this program writes the entry line to /output/entry.txt.
"""

from pathlib import Path

OUTPUT_PATH = Path("/output/entry.txt")

COMPLAINT = "The printer only jams when the document is urgent, "
REFRAME = "which means technically it's the only one here who understands prioritization."

ENTRY = COMPLAINT + REFRAME


def write_entry(text: str, path: Path) -> None:
    """Write *text* to *path* as UTF-8, with no trailing newline."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def main() -> None:
    """Write the entry line to the fixed output path."""
    write_entry(ENTRY, OUTPUT_PATH)


if __name__ == "__main__":
    main()
