def load_input(as_ints: bool = None, as_strings: bool = None) -> list:
    if as_ints:
        with open("input.txt", "r") as f:
            return [int(lines) for lines in f]

    elif as_strings:
        with open("input.txt", "r") as f:
            return [lines.replace("\n", "") for lines in f]

    else:
        with open("input.txt", "r") as f:
            return [lines for lines in f]
