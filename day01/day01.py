import timeit

def read_file(file_path):
    with open(file_path, "r") as file:
        data = file.read()
        return data

def problem_one(data):
    list_1 = []
    list_2 = []
    total = 0
    for line in data.splitlines():
        list_1.append(line.split("   ")[0])
        list_2.append(line.split("   ")[1])
    list_1.sort()
    list_2.sort()
    for i in range(len(list_1)):
        total += abs(int(list_1[i])-int(list_2[i]))
    return total


def problem_two(data):
    list_1 = []
    list_2 = []
    total = 0
    for line in data.splitlines():
        list_1.append(line.split("   ")[0])
        list_2.append(line.split("   ")[1])
    for line in list_1:
        similarity = list_2.count(line)
        total += similarity * int(line)
    return total


if __name__ == "__main__":
    data01 = read_file("day01/1.txt")
    data02 = read_file("day01/example.txt")
    start_1 = timeit.default_timer()
    answer_1 = problem_one(data01)
    print(f"Part 1: {answer_1}")
    stop_1 = timeit.default_timer()
    print(f"Func took {round((stop_1 - start_1),4)*1000} milliseconds")
    start_2 = timeit.default_timer()
    answer_2 = problem_two(data01)
    print(f"Part 2: {answer_2}")
    stop_2 = timeit.default_timer()
    print(f"Func took {round((stop_2 - start_2),4)*1000} milliseconds")
