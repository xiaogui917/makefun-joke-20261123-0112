import os
from pathlib import Path

JOKE = (
    "Working beside an AI coding agent is great: it writes five hundred "
    "lines of code in two seconds, and then we both wait for the live demo "
    "to find out what it does.\n"
)


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    entry_path = output_dir / "entry.txt"
    entry_path.write_text(JOKE, encoding="utf-8")

    # Verify that the entry file was written successfully and matches expected byte length
    written_bytes = entry_path.stat().st_size
    expected_bytes = len(JOKE.encode("utf-8"))
    if written_bytes != expected_bytes:
        raise OSError(f"Size mismatch: expected {expected_bytes} bytes, wrote {written_bytes}")


if __name__ == "__main__":
    main()
