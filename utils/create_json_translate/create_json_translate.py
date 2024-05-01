import json
import os


def create_json_translate():
    path = "./../../datasets/yoga82/train"
    data = dict()
    for index, folder in enumerate(os.listdir(path)):
        if os.path.isdir(os.path.join(path, folder)):
            data[index] = {
                "english": str(folder),
                "russian": ""
            }

    with open("translate.json", "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    create_json_translate()