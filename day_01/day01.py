
def load_input():
    with open("input.txt", "r") as f:
        return [int(lines) for lines in f]


def part_one(values: list):
    for x in values:
        for y in values:
            if x + y == 2020:
                return x * y


def part_two(values: list):
    for x in values:
        for y in values:
            for z in values:
                if x + y + z == 2020:
                    return x * y * z


if __name__ == '__main__':
    inp = load_input()
    print(part_one(inp))
    print(part_two(inp))
