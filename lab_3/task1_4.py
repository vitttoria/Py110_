INPUT_FILE = "input.txt"
OUTPUT_FILE = "output.txt"


def task():
    with open(INPUT_FILE) as f:
        with open(OUTPUT_FILE, "w", encoding="utf-8") as file_:
            for word in f:
                word = "".join(map(str.upper, word))
                file_.write(word)


if __name__ == "__main__":
    task()

    with open(OUTPUT_FILE) as file:
        for line in file:
            print(line, end="")
