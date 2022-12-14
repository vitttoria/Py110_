import json


def task():
    filename = "input.json"
    with open(filename) as f:
        json_file = json.load(f)
        max_value = max(json_file, key=lambda value: value["score"])
        return max_value


if __name__ == "__main__":
    print(task())
