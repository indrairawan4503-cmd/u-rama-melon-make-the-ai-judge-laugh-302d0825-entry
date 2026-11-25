import os

JOKE = "I set my out-of-office reply for one week; it has since answered 214 emails, chaired a standup, and been promoted above me."


def main():
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
