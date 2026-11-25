from pathlib import Path

# Dying battery's last text to its charger (make.fun bounty entry).
LINE = "Not Low Power Mode—a breakup text. You were my only charger. Screen fading. Going dark."


def main() -> None:
    """Write LINE to /output/entry.txt for the make.fun evaluator."""
    assert isinstance(LINE, str), "LINE must be a string"
    assert 1 <= len(LINE) <= 200, "LINE must be 1–200 characters"
    assert "\n" not in LINE, "LINE must be a single line"
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
