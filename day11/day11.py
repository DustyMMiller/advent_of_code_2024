import timeit

def read_file(file_path):
    with open(file_path, "r") as file:
        data = file.read()
        return data

def evaluate_stones(stones):
    stones.sort(key=lambda tup: tup[0])
    stone_tuples = []
    stone_tuples.append(stones[0])
    for stone in stones[1:]:
        if stone_tuples[-1][0] == stone[0]:
            stone_tuples[-1] = (stone_tuples[-1][0], stone_tuples[-1][1] + stone[1])
        else:
            stone_tuples.append(stone)
    return stone_tuples

def blink(stones):
    stones = evaluate_stones(stones)
    new_stones = []
    for number in stones:
        if int(number[0]) == 0:
            new_stones.append(("1", number[1]))
        elif len(number[0]) % 2 == 0:
            split_spot = int(len(number[0]) / 2)
            left = number[0][:split_spot].lstrip("0")
            right = number[0][split_spot:].lstrip("0")
            if right == "":
                right = "0"
            new_stones.append((left, number[1]))
            new_stones.append((right, number[1]))
        else:
            new_stones.append((str(int(number[0]) * 2024), number[1]))
    return new_stones


def problem(data, blinks):
    stones = data.strip("\n").split(" ")
    stone_tuples = []
    total = 0
    for stone in stones:
        stone_tuples.append((stone, 1))
    stone_tuples = evaluate_stones(stone_tuples)
    for x in range(blinks):
        stone_tuples = blink(stone_tuples)

    for stone in stone_tuples:
        total += stone[1]

    return total

if __name__ == "__main__":
    data01 = read_file("day11/1.txt")
    data02 = read_file("day11/example.txt")
    for x in range(1000):
        start = timeit.default_timer()
        answer = problem(data01, x)
        print(f"Part {x}: {answer}")
        stop = timeit.default_timer()
        print(f"Func took {round(stop - start,4)*1000} milliseconds")
