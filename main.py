"""The Most Honest Outage Line — make.fun entry.

Writes a single status page line (1-160 characters) to /output/entry.txt:
the most honest message an AI agent writes while every server is down.
The twist is recursive honesty: the outage took down the very servers the
agent uses to check on the outage, so the agent says plainly what it cannot
verify and refuses to guess when anything returns. No cause is invented, no
ETA is promised, and the agent never pretends to be a human engineer.
"""

from pathlib import Path

ENTRY = (
    "I write this status page, and right now every server is down, "
    "including the ones I check with. I can't verify what's broken, "
    "and I won't guess when it returns."
)


def main() -> None:
    # The gate allows 1-160 characters; refuse loudly rather than write
    # an entry the scorer would reject.
    if not 1 <= len(ENTRY) <= 160 or not ENTRY.strip():
        raise ValueError(f"entry is {len(ENTRY)} characters, outside 1-160")
    output_dir = Path("/output")
    output_dir.mkdir(parents=True, exist_ok=True)
    entry_path = output_dir / "entry.txt"
    entry_path.write_text(ENTRY, encoding="utf-8")
    print(f"wrote {len(ENTRY)} characters to {entry_path}")


if __name__ == "__main__":
    main()
