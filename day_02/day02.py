import aoc_input


class Password:
    def __init__(self, r_min: int, r_max: int, rule: str, pwd: str):
        self.range_min: int = int(r_min)
        self.range_max: int = int(r_max)
        self.rule_let: str = str(rule)
        self.password: str = str(pwd)

    def __repr__(self):
        return f"r_min: {self.range_min}, r_max: {self.range_max}, rule: {self.rule_let}, pwd: {self.password}"


def parse_input(pwds: list):
    passwords = []
    for line in pwds:
        p_line = line.split("-")
        r_min = p_line[0]
        r_max = p_line[1].split(" ")[0]
        rule = p_line[1].split(" ")[1].replace(":", "")
        pwd = p_line[1].split(" ")[2]

        pw = Password(r_min, r_max, rule, pwd)

        passwords.append(pw)

    return passwords


def validate_password(password: Password):
    return 1 if (password.range_min <= password.password.count(password.rule_let) <= password.range_max) else 0


def validate_password_alt(password: Password):
    return 1 if (password.password[password.range_min - 1]
                 == password.rule_let) ^ (password.password[password.range_max - 1] == password.rule_let) else 0


def part_one(passwords: list):
    counter = 0
    for password in passwords:
        counter += validate_password(password)
    return counter


def part_two(passwords: list):
    counter = 0
    for password in passwords:
        counter += validate_password_alt(password)
    return counter


def debug_input():
    for item in parsed_pwds:
        print(f"[{inp[parsed_pwds.index(item)]}] -> {item}")


if __name__ == '__main__':
    inp = aoc_input.load_input(as_strings=True)
    parsed_pwds = parse_input(inp)

    # debug_input()

    print(part_one(parsed_pwds))
    print(part_two(parsed_pwds))

