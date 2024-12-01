def read_file(file_path):
    with open(file_path, "r") as file:
        data = file.read()
        return data

def problem_one(data):
    list_1 = []
    list_2 = []
    total = 0
    for line in data.splitlines():
        list_1.append(line.split("   ")[0])
        list_2.append(line.split("   ")[1])
    list_1.sort()
    list_2.sort()
    for i in range(len(list_1)):
        total += abs(int(list_1[i])-int(list_2[i]))
    print(total)


def problem_two(data):
    list_1 = []
    list_2 = []
    total = 0
    for line in data.splitlines():
        list_1.append(line.split("   ")[0])
        list_2.append(line.split("   ")[1])
    for line in list_1:
        similarity = list_2.count(line)
        total += similarity * int(line)
    print(total)


if __name__ == "__main__":
    data01 = read_file("day01/1.txt")
    data02 = read_file("day01/1.txt")
    problem_one(data01)
    problem_two(data02)
