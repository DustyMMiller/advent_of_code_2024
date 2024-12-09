import numpy as np
import timeit

def compact_file(file_map):
    for key, value in enumerate(file_map):
        if value == ".":
            new_value, x = get_last_file(file_map)
            if file_map.shape[0]-x > key:
                file_map[key] = new_value
                file_map[-x-1] = "."
            else:
                return 0

def get_last_file(file_map):
    file = 0
    for x in range(file_map.shape[0]-1):
        if file_map[-x-1] != ".":
            file = file_map[-x-1]
            return file, x

def move_file(file_map, current_file, current_file_length, current_x):
    free_space = 0
    for key, value in enumerate(file_map):
        if value == ".":
            free_space += 1
            if free_space == current_file_length and key < file_map.shape[0] - current_x:
                for x in range(current_file_length):
                    file_map[key-x] = current_file
                    file_map[-current_x+x] = "."
                return 0
        else:
            free_space = 0

def calculate_checksum(file_map):
    total = 0
    for key, value in enumerate(file_map):
        if value != ".":
            total += int(value)*key
    return total

def read_file(file_path):
    with open(file_path, "r") as file:
        data = file.read()
        return data

def problem_one(data):
    file_map = []
    for x in range(len(data)-1):
        for y in range(int(data[x])):
            if x % 2 == 0:
                file_map.append(int(x/2))
            else:
                file_map.append(".")
    file_map = np.array(file_map)
    compact_file(file_map)
    total = calculate_checksum(file_map)
    return total

def problem_two(data):
    file_map = []
    for x in range(len(data)-1):
        for y in range(int(data[x])):
            if x % 2 == 0:
                file_map.append(int(x/2))
            else:
                file_map.append(".")
    file_map = np.array(file_map)
    current_file = ''
    current_file_length = 1
    for x in range(file_map.shape[0]-1):
        if current_file != file_map[-x-1]:
            if x > 0 and current_file != ".":
                move_file(file_map, current_file, current_file_length, x)
            current_file = file_map[-x-1]
            current_file_length = 1
        else:
            current_file_length += 1
    total = calculate_checksum(file_map)
    return total


if __name__ == "__main__":
    data01 = read_file("day09/1.txt")
    data02 = read_file("day09/example.txt")
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
