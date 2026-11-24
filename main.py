"""One Line, One Chill — make.fun entry.

Writes a single sentence of horror (one line, under 200 characters)
to /output/entry.txt. Deterministic: the line is a fixed constant,
no randomness, no time, no input.
"""

import os

ENTRY = "The tide returned my father's shoe, still laced, and the wet footprints led from the water to my front door."


def main() -> None:
    # Gate self-check: the sealed scorer requires UTF-8 text of
    # 1 to 200 characters, not only white space, a single sentence.
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    assert ENTRY.strip(), "entry must not be only white space"
    assert ENTRY.count(".") == 1 and ENTRY.endswith("."), (
        "entry must be exactly one sentence"
    )
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"Wrote {len(ENTRY)} characters to {path}")


if __name__ == "__main__":
    main()
