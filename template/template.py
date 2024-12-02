def read_file(file_path):
    with open(file_path, "r") as file:
        data = file.read()
        return data

def problem_one(data):
    #for line in data.splitlines():
    pass

def problem_two(data):
    #for line in data.splitlines():
    pass


if __name__ == "__main__":
    data01 = read_file("day01/1.txt")
    data02 = read_file("day01/example.txt")
    problem_one(data02)
    problem_two(data02)

