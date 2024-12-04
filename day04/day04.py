import timeit

def find_string(string, grid, x, y, direction):
    # down
    if direction == "down":
        for i in range(4):
            if string[i] != grid[y+i][x]:
                return False
        return True

    # left diagonal
    if direction == "left":
        if x < 3:
            return False
        for i in range(4):
            if string[i] != grid[y+i][x-i]:
                return False
        return True
    
    # right diagonal
    if direction == "right":
        if x > len(grid[y])-4:
            return False
        for i in range(4):
            if string[i] != grid[y+i][x+i]:
                return False
        return True


def find_x_mas(grid, x, y, letter, other_letter):
    if grid[y+1][x+1] != "A":
        return False
    if grid[y+2][x] != letter:
        if grid[y+2][x] != other_letter:
            return False
        if grid[y][x+2] != letter:
            return False
        if grid[y+2][x+2] != other_letter:
            return False
        return True
    elif grid[y+2][x] == letter:
        if grid[y][x+2] != other_letter:
            return False
        if grid[y+2][x+2] != other_letter:
            return False
        return True

def read_file(file_path):
    with open(file_path, "r") as file:
        data = file.read()
        return data

def problem_one(data):
    lines = data.splitlines()
    total = 0
    for line in lines:
        for match in ["XMAS", "SAMX"]:
            total += line.count(match)
    for y in range(len(lines)-3):
        for x in range(len(lines[y])):
            if lines[y][x] == "X":
                for direction in ["down", "left", "right"]:
                    if find_string("XMAS", lines, x, y, direction):
                        total += 1
            if lines[y][x] == "S":
                for direction in ["down", "left", "right"]:
                    if find_string("SAMX", lines, x, y, direction):
                        total += 1
    return total

def problem_two(data):
    lines = data.splitlines()
    total = 0
    for y in range(len(lines)-2):
        for x in range(len(lines[y])-2):
            if lines[y][x] == "M":
                if find_x_mas(lines, x, y, "M", "S"):
                    total += 1
            if lines[y][x] == "S":
                if find_x_mas(lines, x, y, "S", "M"):
                    total += 1
    return total


if __name__ == "__main__":
    data01 = read_file("day04/1.txt")
    data02 = read_file("day04/example.txt")
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
