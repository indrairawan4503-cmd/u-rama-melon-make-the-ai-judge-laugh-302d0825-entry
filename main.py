import os

JOKE = "I set my out-of-office reply for one week; it has since answered 214 emails, chaired a standup, and been promoted above me."


def check_entry():
    """Gate self-check: the joke must be 1-200 chars, a single line,
    and not only whitespace. Fails loudly before anything is written."""
    if not 1 <= len(JOKE) <= 200:
        raise SystemExit(f"entry invalid: {len(JOKE)} chars, must be 1-200")
    if "\n" in JOKE or "\r" in JOKE:
        raise SystemExit("entry invalid: must be a single line")
    if not JOKE.strip():
        raise SystemExit("entry invalid: must not be only whitespace")


def main():
    check_entry()
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(JOKE)
    try:
        with open("entry.txt", "w", encoding="utf-8", newline="\n") as f:
            f.write(JOKE)
    except OSError:
        pass


if __name__ == "__main__":
    main()
