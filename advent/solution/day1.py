input = open('advent/resources/day_01.txt','r').read()


def solution(input):
    """Parse input"""
    elves_calories = [0]
    for line in input.split("\n"):
        if line.strip():
            elves_calories[-1] += int(line)
        else:
            elves_calories.append(0)
    elves_calories.sort()
    return elves_calories[-1], sum(elves_calories[-3:])

def solve():
    result = solution(input)
    print("============")
    print("DAY ONE")
    print(f"Part 1: {result[0]} \nPart 2: {result[1]}")

if __name__ == "__main__":
    solve()