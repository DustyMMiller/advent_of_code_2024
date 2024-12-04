import timeit
import re

mul_match = re.compile(r"mul\((\d{1,3},\d{1,3})\)")
all_match = re.compile(r"(?P<first>^.*?)don't\(\)(?P<second>.*?)do\(\)(?P<third>(?:(?!don't\(\)).)*)$")
do_match = re.compile(r"do\(\)(.*?)don't\(\)")

def get_matches(data):
    matches = []
    parts = all_match.search(data)
    matches += mul_match.findall(parts.group("first"))
    for match in do_match.findall(parts.group("second")):
        matches += mul_match.findall(match)
    matches += mul_match.findall(parts.group("third"))
    return matches

def read_file(file_path):
    with open(file_path, "r") as file:
        data = file.read()
        return data

def problem_one(data):
    matches = mul_match.findall(data)
    total = 0
    for match in matches:
        x, y = match.split(",")
        x = int(x)
        y = int(y)
        total += x * y
    return total

def problem_two(data):
    data = data.replace("\n", "")
    matches = get_matches(data)
    total = 0
    for match in matches:
        x, y = match.split(",")
        total += int(x) * int(y)
    return total


if __name__ == "__main__":
    data01 = read_file("day03/1.txt")
    data02 = read_file("day03/example.txt")
    data03 = read_file("day03/example2.txt")
    start_1 = timeit.default_timer()
    answer_1 = problem_one(data01)
    print(f"Part 1: {answer_1}")
    stop_1 = timeit.default_timer()
    print(f"Func took {round(stop_1 - start_1,4)*1000} milliseconds")
    start_2 = timeit.default_timer()
    answer_2 = problem_two(data01)
    print(f"Part 2: {answer_2}")
    stop_2 = timeit.default_timer()
    print(f"Func took {round(stop_2 - start_2,4)*1000} milliseconds")
