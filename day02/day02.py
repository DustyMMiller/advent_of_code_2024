import timeit

def read_file(file_path):
    with open(file_path, "r") as file:
        data = file.read()
        return data

def problem_one(data):
    safe_levels = 0
    for line in data.splitlines():
        levels = line.split(" ")
        if check_levels(levels):
            safe_levels += 1
    return safe_levels

def problem_two(data):
    safe_levels = 0
    for line in data.splitlines():
        levels_array = line.split(" ")
        levels_to_check = []
        levels_to_check.append(levels_array)
        for i in range(len(levels_array)):
            current_array = levels_array.copy()
            current_array.pop(i)
            levels_to_check.append(current_array)
        for levels in levels_to_check:
            if check_levels(levels):
                safe_levels += 1
                break
    return safe_levels

def check_levels(levels):
    prev_level = ""
    # 0 = down, 1 = up
    direction = 0
    for i in range(len(levels)):
        if i > 1:
            current_direction = direction
            if abs(int(prev_level) - int(levels[i])) < 4:
                if prev_level > int(levels[i]):
                    direction = 0
                elif prev_level < int(levels[i]):
                    direction = 1
                else:
                    return False
                if current_direction != direction:
                    return False
            else:
                return False
            prev_level = int(levels[i])
        else:
            if i == 1:
                if abs(int(prev_level) - int(levels[i])) < 4:
                    if int(prev_level) > int(levels[i]):
                        direction = 0
                    elif int(prev_level) < int(levels[i]):
                        direction = 1
                    else:
                        return False
                else:
                    return False
            prev_level = int(levels[i])
    return True

if __name__ == "__main__":
    data01 = read_file("day02/1.txt")
    data02 = read_file("day02/example.txt")
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
