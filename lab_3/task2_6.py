import json


def task():
    filename = "input.json"
    with open(filename) as f:
        json_data = json.load(f)
        # with open("output_file", "w") as file_:
        #     sorted_file = sorted(json_data, key=lambda value: value["length"])
        # write_file = json.dumps(sorted_file)
        # file_.write(write_file)

    # return write_file
    return sorted(json_data, key=lambda value: value["length"])


if __name__ == "__main__":
    data = task()
    print(json.dumps(data, indent=4))

    # TODO дополнительно записать отсортированный список в JSON файл
