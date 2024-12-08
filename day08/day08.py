import numpy as np
import timeit

def read_file(file_path):
    with open(file_path, "r") as file:
        data = file.read()
        return data
    
def get_antinodes(location_1, location_2, direction, inc, shape):
    x = location_1[0]-location_2[0]
    y = location_1[1]-location_2[1]
    antinodes = []
    if direction == 0:
        antinode = (location_1[0] + x*inc, location_1[1] + y*inc)
    else:
        antinode = (location_2[0] - x*inc, location_2[1] - y*inc)
    if antinode[0] >= 0 and antinode[1] >= 0 and antinode[0] < shape[0] and antinode[1] < shape[0]:
        antinodes.append(antinode)
    return antinodes

def problem_one(data):
    antennas = {}
    map = []
    antinodes = []
    for line in data.splitlines():
        map.append(list(line))
    map = np.array(map)

    for index, value in np.ndenumerate(map):
        if value != '.':
            if str(value) not in antennas:
                antennas[str(value)] = []
            antennas[str(value)].append(index)
    for key in antennas:
        for i in range(len(antennas[key])):
            for location in antennas[key][i+1:]:
                nodes = []
                for x in range(2):
                    returned_nodes = get_antinodes(antennas[key][i], location, x, 1, map.shape)
                    if returned_nodes:
                        nodes += returned_nodes
                for node in nodes:
                    if node not in antinodes:
                        antinodes.append(node)
    return len(antinodes)

def problem_two(data):
    antennas = {}
    map = []
    antinodes = []
    for line in data.splitlines():
        map.append(list(line))
    map = np.array(map)

    for index, value in np.ndenumerate(map):
        if value != '.':
            if str(value) not in antennas:
                antennas[str(value)] = []
            antennas[str(value)].append(index)
    for key in antennas:
        for i in range(len(antennas[key])):
            for location in antennas[key][i+1:]:
                nodes = []
                for x in range(2):
                    y = 0
                    while True:
                        returned_nodes = get_antinodes(antennas[key][i], location, x, y, map.shape)
                        if returned_nodes:
                            nodes += returned_nodes
                        if not returned_nodes:
                            break
                        y += 1
                for node in nodes:
                    if node not in antinodes:
                        antinodes.append(node)
    
    return len(antinodes)


if __name__ == "__main__":
    data01 = read_file("day08/1.txt")
    data02 = read_file("day08/example.txt")
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
