import copy
import timeit

directions = ["up", "right", "down", "left"]

def read_file(file_path):
    with open(file_path, "r") as file:
        data = file.read()
        return data

def obstactle_moves(grid, guard, current_direction):
    history = []
    if not grid:
        return False
    while True:
        move = move_guard(guard, grid, directions[current_direction])
        spot = guard + [current_direction]
        match move:
            case "Done":
                return False
            case "Turn":
                if spot in history:
                    return True
                if current_direction == 3:
                    current_direction = 0
                else:
                    current_direction += 1
            case _:
                guard = move
        history.append(spot)

def add_obstacle(grid, x, y, direction):
    match direction:
        # up
        case "up":
            if y == 0:
                return False
            grid[y-1][x] = "#"
        # down
        case "down":
            if y == len(grid)-1:
                return False
            grid[y+1][x] = "#"
        # left
        case "left":
            if x == 0:
                return False
            grid[y][x-1] = "#"
        # right
        case "right":
            if x == len(grid[0])-1:
                return False
            grid[y][x+1] = "#"
    return grid

def move_guard(guard, grid, direction):
    match direction:
        # up
        case "up":
            if guard[1] == 0:
                return "Done"
            if grid[guard[1]-1][guard[0]] == "#":
                return "Turn"
            return [guard[0], guard[1]-1]
        # down
        case "down":
            if guard[1] == len(grid[1])-1:
                return "Done"
            if grid[guard[1]+1][guard[0]] == "#":
                return "Turn"
            return [guard[0],guard[1]+1]
        # left
        case "left":
            if guard[0] == 0:
                return "Done"
            if grid[guard[1]][guard[0]-1] == "#":
                return "Turn"
            return [guard[0]-1,guard[1]]
        # right
        case "right":
            if guard[0] == len(grid)-1:
                return "Done"
            if grid[guard[1]][guard[0]+1] == "#":
                return "Turn"
            return [guard[0]+1,guard[1]]

def problem_one(data):
    lines = data.splitlines()
    for line in range(len(lines)):
        lines[line] = list(lines[line])
    total = 0
    guard = [0,0]
    current_direction = 0
    for y in range(len(lines)):
        for x in range(len(lines[y])):
            if lines[y][x] == "^":
                guard = [x,y]
    while True:
        move = move_guard(guard, lines, directions[current_direction])
        if move == "Done":
            lines[guard[1]][guard[0]] = "X"
            break
        if move == "Turn":
            if current_direction == 3:
                current_direction = 0
            else:
                current_direction += 1
        else:
            lines[guard[1]][guard[0]] = "X"
            guard = move

    total = sum([x.count("X") for x in lines])

    return total

def problem_two(data):
    lines = data.splitlines()
    for line in range(len(lines)):
        lines[line] = list(lines[line])
    guard = []
    starting_position = []
    path = []
    obstacles = []
    current_direction = 0
    for y in range(len(lines)):
        for x in range(len(lines[y])):
            if lines[y][x] == "^":
                guard = [x,y]
                starting_position = [x,y]
                lines[y][x] = "."
    while True:
        spot = guard
        if spot not in path:
            path.append(spot)
        move = move_guard(guard, lines, directions[current_direction])
        if move == "Done":
            break
        if move == "Turn":
            if current_direction == 3:
                current_direction = 0
            else:
                current_direction += 1
        else:
            guard = move
    for spot in path[1:]:
        grid = copy.deepcopy(lines)
        grid[spot[1]][spot[0]] = "#"
        if obstactle_moves(grid, [starting_position[0], starting_position[1]], 0):
            if [spot[0], spot[1]] not in obstacles:
                obstacles.append([spot[0], spot[1]])
    return len(obstacles)


if __name__ == "__main__":
    data01 = read_file("day06/1.txt")
    data02 = read_file("day06/example.txt")
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
