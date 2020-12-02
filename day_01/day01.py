import aoc_input


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
    inp = aoc_input.load_input(as_ints=True)
    print(part_one(inp))
    print(part_two(inp))
