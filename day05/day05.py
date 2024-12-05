import timeit

def evaulate_orders(rules, line, fix=False, fixed=False):
    for i in range(len(line)-1):
        if fix:
            order = lookup_orders(rules, line[i], line[i+1:], True)
            if isinstance(order, list):
                fixed=True
                replace1 = line[i]
                replace2 = line[line.index(order[1])+order[0]+1]
                line[line.index(order[1])+order[0]+1] = replace1
                line[i] = replace2
                evaulate_orders(rules, line, True, True)
            else:
                continue
        if not lookup_orders(rules, line[i], line[i+1:]):
            return False
    if fixed:
        return line
    return True

def lookup_orders(rules, order1, orders, fix=False):
    for i in range(len(orders)):
        if not lookup_order(rules, order1, orders[i]):
            if fix:
                return [i, order1]
            return False
    return True

def lookup_order(rules, order1, order2):
    for rule in rules:
        if order1 == rule[0] and order2 == rule[1]:
            return True
    return False

def read_file(file_path):
    with open(file_path, "r") as file:
        data = file.read()
        return data

def problem_one(data):
    rules = []
    orders = []
    total = 0
    for line in data.splitlines():
        if "|" in line:
            rule = line.split("|")
            rules.append(rule)
        elif "," in line:
            orders.append(line)
    for line in orders:
        line = line.split(",")
        if evaulate_orders(rules, line):
            middle = int(len(line)/2)
            total += int(line[middle])
    return total

def problem_two(data):
    rules = []
    orders = []
    total = 0
    for line in data.splitlines():
        if "|" in line:
            rule = line.split("|")
            rules.append(rule)
        elif "," in line:
            orders.append(line)
    for line in orders:
        line = line.split(",")
        fixed = evaulate_orders(rules, line, True)
        if isinstance(fixed, list):
            middle = int(len(line)/2)
            total += int(line[middle])
    return total


if __name__ == "__main__":
    data01 = read_file("day05/1.txt")
    data02 = read_file("day05/example.txt")
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
