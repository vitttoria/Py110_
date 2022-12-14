OUTPUT_FILE = "output.txt"


def task():
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        for i in range(1, 11, 1):
            stars = i * "*"
            stars = stars.rjust(10)
            f.write(stars+"\n")


if __name__ == "__main__":
    task()

    with open(OUTPUT_FILE) as file:
        for line in file:
            print(line, end="")
