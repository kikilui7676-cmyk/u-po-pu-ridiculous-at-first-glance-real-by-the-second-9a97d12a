import os
from pathlib import Path

LINE = (
    "Silence, sold by the hour: soundproof booths in airports where frazzled "
    "flyers pay $40 to sit in actual quiet, and airlines underwrite the booths "
    "because calm passengers complain 30% less."
)


def main() -> None:
    out = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out.mkdir(parents=True, exist_ok=True)
    (out / "entry.txt").write_text(LINE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
