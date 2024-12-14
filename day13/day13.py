import re
import timeit

button_re = re.compile(r"Button ([A-Z]+)\: X\+(\d+), Y\+(\d+)")
machine_re = re.compile(r"Prize\: X=(\d+), Y=(\d+)")

def read_file(file_path):
    with open(file_path, "r") as file:
        data = file.read()
        return data
    
def solve_button(a, b, c):
    solutions = []
    for i in range(1, 100):
        answer = (c - (a*i)) / b
        if answer.is_integer():
            solutions.append((i, int(answer)))
    return solutions

def read_machines(data, conv=False):
    machines = []
    i = 0
    current_machine = []
    for line in data.splitlines():
        if i % 4 == 0:
            current_machine = []
            machines.append(current_machine)
        if line != '':
            button = button_re.match(line)
            machine = machine_re.match(line)
            if button:
                button = (button.group(1), int(button.group(2)), int(button.group(3)))
                current_machine.append(button)
            if machine:
                if conv:
                    machine = (int(machine.group(1))+10000000000000, int(machine.group(2))+10000000000000)
                else:
                    machine = (int(machine.group(1)), int(machine.group(2)))
                current_machine.append(machine)
        i += 1
    return machines

def find_tokens(machine):
    solutions = []
    X = solve_button(machine[0][1], machine[1][1], machine[2][0])
    Y = solve_button(machine[0][2], machine[1][2], machine[2][1])
    for x in X:
        if x in Y:
            solutions.append((x[0] * 3) + x[1])
    solutions.sort()
    if solutions:
        return solutions[0]
    return 0

def problem_one(data):
    machines = read_machines(data)
    total = 0
    for machine in machines:
        total += find_tokens(machine)

    return total

def problem_two(data):
    machines = read_machines(data, True)
    total = 0
    for machine in machines:
        a = (machine[0][1] * machine[1][1], machine[0][2] * machine[1][1])

    return total


if __name__ == "__main__":
    data01 = read_file("day13/1.txt")
    data02 = read_file("day13/example.txt")
    start_1 = timeit.default_timer()
    answer_1 = problem_one(data01)
    print(f"Part 1: {answer_1}")
    stop_1 = timeit.default_timer()
    print(f"Func took {round(stop_1 - start_1,4)*1000} milliseconds")
    start_2 = timeit.default_timer()
    answer_2 = problem_two(data02)
    print(f"Part 2: {answer_2}")
    stop_2 = timeit.default_timer()
    print(f"Func took {round(stop_2 - start_2,4)*1000} milliseconds")
