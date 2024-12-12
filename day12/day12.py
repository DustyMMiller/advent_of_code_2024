import numpy as np
import timeit

def read_file(file_path):
    with open(file_path, "r") as file:
        data = file.read()
        return data
    
def build_section(garden, key, value, section):
    if key in section:
        return section
    section.add(key)
    # up
    if key[1] > 0:
        if garden[key[0], key[1]-1] == value:
            build_section(garden, (key[0], key[1]-1), value, section)
    # down
    if key[1] < garden.shape[1]-1:
        if garden[key[0], key[1]+1] == value:
            build_section(garden, (key[0], key[1]+1), value, section)
    # left
    if key[0] > 0:
        if garden[key[0]-1, key[1]] == value:
            build_section(garden, (key[0]-1, key[1]), value, section)
    # right
    if key[0] < garden.shape[0]-1:
        if garden[key[0]+1, key[1]] == value:
            build_section(garden, (key[0]+1, key[1]), value, section)
    garden[key] = "0"
    return section

def calculate_perimeter(section):
    perimeter = 0
    for item in section:
        perimeter += 4
        if (item[0]-1, item[1]) in section:
            perimeter -= 1
        if (item[0]+1, item[1]) in section:
            perimeter -= 1
        if (item[0], item[1]-1) in section:
            perimeter -= 1
        if (item[0], item[1]+1) in section:
            perimeter -= 1
    return perimeter

def evaluate_section(garden, key, value, discount=False):
    section = set()
    build_section(garden, key, value, section)
    area = len(section)
    if discount:
        sides = calculate_sides(section)
        return area * sides
    perimeter = calculate_perimeter(section)
    return area * perimeter

def calculate_sides(section):
    sides = 0
    checked_item = []
    section = list(section)
    section.sort(key=lambda x: (x[0], x[1]))
    for item in section:
        if (item[0]-1, item[1]) in section:
            if (item[0], item[1]+1) in section and (item[0], item[1]-1) in section:
                if ((item[0]+1, item[1]), "up") in checked_item or ((item[0]-1, item[1]), "up") in checked_item:
                    pass
        else:
            checked_item.append((item,"up"))
            if ((item[0], item[1]+1), 'up') not in checked_item and ((item[0], item[1]-1), 'up') not in checked_item:
                sides += 1

        if (item[0]+1, item[1]) in section:
            if (item[0], item[1]+1) in section and (item[0], item[1]-1) in section:
                if ((item[0]+1, item[1]), "down") in checked_item or ((item[0]-1, item[1]), "down") in checked_item:
                    pass
        else:
            checked_item.append((item,"down"))
            if ((item[0], item[1]+1), 'down') not in checked_item and ((item[0], item[1]-1), 'down') not in checked_item:
                sides += 1

        if (item[0], item[1]-1) in section:
            if (item[0]+1, item[1]) in section and (item[0]-1, item[1]) in section:
                if ((item[0], item[1]-1), "left") in checked_item or ((item[0], item[1]+1), "left") in checked_item:
                    pass
        else:
            checked_item.append((item,"left"))
            if ((item[0]+1, item[1]), 'left') not in checked_item and ((item[0]-1, item[1]), 'left') not in checked_item:
                sides += 1

        if (item[0], item[1]+1) in section:
            if (item[0]+1, item[1]) in section and (item[0]-1, item[1]) in section:
                if ((item[0], item[1]-1), "right") in checked_item or ((item[0], item[1]+1), "right") in checked_item:
                    pass
        else:
            checked_item.append((item,"right"))
            if ((item[0]+1, item[1]), 'right') not in checked_item and ((item[0]-1, item[1]), 'right') not in checked_item:
                sides += 1
                
    return sides

def problem_one(data):
    total = 0
    garden = []
    for lines in data.splitlines():
        line = []
        for i in lines:
            line.append(i)
        garden.append(line)
    garden = np.array(garden)
    for key, value in np.ndenumerate(garden):
        if value == "0":
            pass
        else:
            total += evaluate_section(garden, key, value)
    return total

def problem_two(data):
    total = 0
    garden = []
    for lines in data.splitlines():
        line = []
        for i in lines:
            line.append(i)
        garden.append(line)
    garden = np.array(garden)
    for key, value in np.ndenumerate(garden):
        if value == "0":
            pass
        else:
            total += evaluate_section(garden, key, value, discount=True)
    return total


if __name__ == "__main__":
    data01 = read_file("day12/1.txt")
    data02 = read_file("day12/example.txt")
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
