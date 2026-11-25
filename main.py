from pathlib import Path

LINE = "This isn't Low Power Mode—it's a breakup text. You were my only charger. Going dark."


def main() -> None:
    assert isinstance(LINE, str)
    assert 1 <= len(LINE) <= 200 and "\n" not in LINE
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
