input = open("2025/inputs/day_01.txt", "r").read()
test = """L68
L30
R48
L5
R60
L55
L1
L99
R14
L82
"""


def solution(input):
    """Parse input"""
    start = 50
    count = 0
    for val in input.split("\n"):
        if not val:
            continue
        direction = val[0]
        turns = val[1:]
        if direction == "L":
            start = (start - int(turns)) % 100
        elif direction == "R":
            start = (start + int(turns)) % 100
        if start == 0:
            count += 1

    return count, None


def solve():
    result = solution(input)
    print("============")
    print("DAY ONE")
    print(f"Part 1: {result[0]} \nPart 2: {result[1]}")


if __name__ == "__main__":
    solve()
