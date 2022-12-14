INPUT_FILE = "input.txt"


def task() -> None:
    with open(INPUT_FILE) as file:
        for sym in file:
            print(sym, end="")


if __name__ == "__main__":
    task()
