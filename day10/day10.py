import numpy as np
import timeit

a_total = 0
def read_file(file_path):
    with open(file_path, "r") as file:
        data = file.read()
        return data
    
def check_trail(trailhead, key, value, trails, base=None):
    if value == 1:
        trails[key] = []
        base = key
    if key[0]-1 >= 0:
        if trailhead[key[0]-1, key[1]] == value:
            if value == 9:
                trails[base].append((key[0]-1, key[1]))
            check_trail(trailhead, (key[0]-1, key[1]), value+1, trails, base)

    if key[0]+1 < trailhead.shape[0]:
        if trailhead[key[0]+1, key[1]] == value:
            if value == 9:
                trails[base].append((key[0]+1, key[1]))
            check_trail(trailhead, (key[0]+1, key[1]), value+1, trails, base)

    if key[1]-1 >= 0:
        if trailhead[key[0], key[1]-1] == value:
            if value == 9:
                trails[base].append((key[0], key[1]-1))
            check_trail(trailhead, (key[0], key[1]-1), value+1, trails, base)

    if key[1]+1 < trailhead.shape[1]:
        if trailhead[key[0], key[1]+1] == value:
            if value == 9:
                trails[base].append((key[0], key[1]+1))
            check_trail(trailhead, (key[0], key[1]+1), value+1, trails, base)
    if value == 1:
        return len(trails)
    return trails

def problem_one(data):
    trailhead = []
    trails = {}
    total = 0
    for line in data.splitlines():
        x = []
        for i in line:
            x.append(int(i))
        trailhead.append(x)
    trailhead = np.array(trailhead)
    for key, value in np.ndenumerate(trailhead):
        if value == 0:
            check_trail(trailhead, key, 1, trails)
    for key in trails:
        values = set(trails[key])
        for value in values:
            total += 1
    return total

def problem_two(data):
    trailhead = []
    trails = {}
    total = 0
    for line in data.splitlines():
        x = []
        for i in line:
            x.append(int(i))
        trailhead.append(x)
    trailhead = np.array(trailhead)
    for key, value in np.ndenumerate(trailhead):
        if value == 0:
            check_trail(trailhead, key, 1, trails)
    for key in trails:
        for value in trails[key]:
            total += 1
    return total


if __name__ == "__main__":
    data01 = read_file("day10/1.txt")
    data02 = read_file("day10/example.txt")
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
