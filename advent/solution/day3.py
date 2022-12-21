input = open('advent/resources/day_03.txt','r').read()

letter_scores = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
    "e": 5,
    "f": 6,
    "g": 7,
    "h": 8,
    "i": 9,
    "j": 10,
    "k": 11,
    "l": 12,
    "m": 13,
    "n": 14,
    "o": 15,
    "p": 16,
    "q": 17,
    "r": 18,
    "s": 19,
    "t": 20,
    "u": 21,
    "v": 22,
    "w": 23,
    "x": 24,
    "y": 25,
    "z": 26,
    "A": 27,
    "B": 28,
    "C": 29,
    "D": 30,
    "E": 31,
    "F": 32,
    "G": 33,
    "H": 34,
    "I": 35,
    "J": 36,
    "K": 37,
    "L": 38,
    "M": 39,
    "N": 40,
    "O": 41,
    "P": 42,
    "Q": 43,
    "R": 44,
    "S": 45,
    "T": 46,
    "U": 47,
    "V": 48,
    "W": 49,
    "X": 50,
    "Y": 51,
    "Z": 52,
}


def solution(puzzle_input):
    """Parse input"""
    rucksack_items = puzzle_input.split("\n")
    rucksacks_part_1 = [
        "".join(
            set(line[: len(line) // 2]).intersection(
                line[len(line) // 2 :]
            )
        )
        for line in rucksack_items
    ]
    rucksacks_part_2 = [
        "".join(
            set(rucksack_items[current_position])
            .intersection(rucksack_items[current_position + 1])
            .intersection(rucksack_items[current_position + 2])
        )
        for current_position in range(0, len(rucksack_items), 3)
    ]
    total_score1 = 0
    total_score2 = 0
    for i in rucksacks_part_1:
        if i in letter_scores:
            total_score1 += letter_scores[i]
    for i in rucksacks_part_2:
        if i in letter_scores:
            total_score2 += letter_scores[i]

    return total_score1, total_score2


def solve():
    result = solution(input)
    print("============")
    print("DAY Three")
    print(f"Part 1: {result[0]} \nPart 2: {result[1]}")


if __name__ == "__main__":
    solve()