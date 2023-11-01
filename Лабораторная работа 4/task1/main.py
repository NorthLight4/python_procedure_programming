# TODO решите задачу
import json

FILENAME = "input.json"

def task() -> float:
    with open(FILENAME, "r") as input_json:
        data = json.load(input_json)
        multiplication_list = [dict_iter["score"] * dict_iter["weight"] for dict_iter in data]
        return round(sum(multiplication_list),3)


print(task())
