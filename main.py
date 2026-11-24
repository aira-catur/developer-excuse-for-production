#!/usr/bin/env python3
"""Write a one-line developer excuse for production breakage to entry.txt."""

import os

TEXT = "I cleared the cache to fix it — turns out the cache was the database, we just called it a cache so nobody panicked."


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT + "\n")


if __name__ == "__main__":
    main()
