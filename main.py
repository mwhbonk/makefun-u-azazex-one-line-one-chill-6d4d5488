"""One Line, One Chill — a single-sentence horror line.

The program writes exactly one line of horror to /output/entry.txt:
a single sentence, under 200 characters, that has to frighten a reader
in one breath. No setup, no paragraph, no second chance.
"""

import os

LINE = (
    "Our new house has a nursery wallpapered in crayon drawings "
    "of me sleeping, each one dated tomorrow."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    output_path = os.path.join(output_dir, "entry.txt")
    os.makedirs(output_dir, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as handle:
        handle.write(LINE)


if __name__ == "__main__":
    main()
