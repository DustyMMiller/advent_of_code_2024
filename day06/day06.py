import copy
import timeit

directions = ["up", "right", "down", "left"]

def read_file(file_path):
    with open(file_path, "r") as file:
        data = file.read()
        return data

def obstactle_moves(grid, guard, current_direction):
    grid = add_obstacle(grid, guard[0], guard[1], directions[current_direction])
    looping_double = []
    if not grid:
        return False
    while True:
        move = move_guard(guard, grid, directions[current_direction])
        match move:
            case "Done":
                return False
            case "Turn":
                match current_direction:
                    case 0:
                        current_direction = 1
                        if grid[guard[1]][guard[0]] == "^":
                            return True
                        if grid[guard[1]][guard[0]] in ["<", ">"]:
                            check = guard + ["^"]
                            if check in looping_double:
                                return True
                            looping_double.append(check)
                        grid[guard[1]][guard[0]] = "^"
                    case 1:
                        current_direction = 2
                        if grid[guard[1]][guard[0]] == ">":
                            return True
                        if grid[guard[1]][guard[0]] in ["^", "v"]:
                            check = guard + [">"]
                            if check in looping_double:
                                return True
                            looping_double.append(check)
                        grid[guard[1]][guard[0]] = ">"
                    case 2:
                        current_direction = 3
                        if grid[guard[1]][guard[0]] == "v":
                            return True
                        if grid[guard[1]][guard[0]] in ["<", ">"]:
                            check = guard + ["v"]
                            if check in looping_double:
                                return True
                            looping_double.append(check)
                        grid[guard[1]][guard[0]] = "v"
                    case 3:
                        current_direction = 0
                        if grid[guard[1]][guard[0]] == "<":
                            return True
                        if grid[guard[1]][guard[0]] in ["^", "v"]:
                            check = guard + [">"]
                            if check in looping_double:
                                return True
                            looping_double.append(check)
                        grid[guard[1]][guard[0]] = "<"
            case _:
                guard = move

def add_obstacle(grid, x, y, direction):
    match direction:
        # up
        case "up":
            if y == 0:
                return False
            grid[y-1][x] = "O"
        # down
        case "down":
            if y == len(grid)-1:
                return False
            grid[y+1][x] = "O"
        # left
        case "left":
            if x == 0:
                return False
            grid[y][x-1] = "O"
        # right
        case "right":
            if x == len(grid[0])-1:
                return False
            grid[y][x+1] = "O"
    return grid

def move_guard(guard, grid, direction):
    match direction:
        # up
        case "up":
            if guard[1] == 0:
                return "Done"
            if grid[guard[1]-1][guard[0]] in ["#", "O"]:
                return "Turn"
            return [guard[0], guard[1]-1]
        # down
        case "down":
            if guard[1] == len(grid[1])-1:
                return "Done"
            if grid[guard[1]+1][guard[0]] in ["#", "O"]:
                return "Turn"
            return [guard[0],guard[1]+1]
        # left
        case "left":
            if guard[0] == 0:
                return "Done"
            if grid[guard[1]][guard[0]-1] in ["#", "O"]:
                return "Turn"
            return [guard[0]-1,guard[1]]
        # right
        case "right":
            if guard[0] == len(grid)-1:
                return "Done"
            if grid[guard[1]][guard[0]+1] in ["#", "O"]:
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
    total = 0
    guard = [0,0]
    obstacles = []
    checked_spots = []
    current_direction = 0
    for y in range(len(lines)):
        for x in range(len(lines[y])):
            if lines[y][x] == "^":
                guard = [x,y]
                lines[y][x] = "X"
    while True:
        spot = guard + [current_direction]
        if spot not in checked_spots:
            obstacle_grid = copy.deepcopy(lines)
            obstacle_guard = copy.deepcopy(guard)
            obstacle_direction = copy.deepcopy(current_direction)
            if obstactle_moves(obstacle_grid, obstacle_guard, obstacle_direction):
                #print(f"Found loop with obstacle at {guard}")
                obstacles.append(guard)
        move = move_guard(guard, lines, directions[current_direction])
        if move == "Done":
            break
        if move == "Turn":
            checked_spots.append(spot)
            if current_direction == 3:
                current_direction = 0
            else:
                current_direction += 1
        else:
            checked_spots.append(spot)
            guard = move

    total = len(obstacles)
    return total


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
