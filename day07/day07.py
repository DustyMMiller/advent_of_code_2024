import copy
import timeit

def read_file(file_path):
    with open(file_path, "r") as file:
        data = file.read()
        return data

def do_math(x, y, op):
    if op == 0:
        return int(x) + int(y)
    if op == 1:
        return int(x) * int(y)
    if op == 2:
        return int(str(x) + str(y))

def problem_one(data):
    total = 0
    for line in data.splitlines():
        answer, variables = line.split(":")
        variables = variables.strip().split()
        vars = copy.deepcopy(variables)
        answer_options = [vars[0]]
        for i in range(len(variables)-1):
            answers = copy.deepcopy(answer_options)
            spot_answers = set()
            for x in range(2):
                for y in answers:
                    spot_answers.add(do_math(y, vars[i+1], x))
            answer_options = spot_answers
        for option in answer_options:
            if option == int(answer):
                total += option
    return total

def problem_two(data):
    total = 0
    for line in data.splitlines():
        answer, variables = line.split(":")
        variables = variables.strip().split()
        vars = copy.deepcopy(variables)
        answer_options = [vars[0]]
        for i in range(len(variables)-1):
            answers = copy.deepcopy(answer_options)
            spot_answers = set()
            for x in range(3):
                for y in answers:
                    spot_answers.add(do_math(y, vars[i+1], x))
            answer_options = spot_answers
        for option in answer_options:
            if option == int(answer):
                total += option
    return total


if __name__ == "__main__":
    data01 = read_file("day07/1.txt")
    data02 = read_file("day07/example.txt")
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
