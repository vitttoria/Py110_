import json


def task():
    filename = "input.json"
    with open(filename) as f:
        json_file = json.load(f)
        gen_exr = (value["contains_improvement_appeals"] for value in json_file)
        return sum(gen_exr)


if __name__ == "__main__":
    print(task())
