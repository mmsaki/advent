input = open('advent/resources/day_06.txt','r').read()

def parse_input(puzzle_input):
    """Parse input"""
    return puzzle_input.split("\n")[0]


def inspect_first_distinct_frame(frame_length):
    current_frame = []
    for index, character in enumerate(parse_input(input), start=1):
        if character in current_frame:
            current_frame = current_frame[
                current_frame.index(character) + 1 :
            ]
        current_frame.append(character)
        if len(current_frame) == frame_length:
            return index

def solve():
    print("============")
    print("DAY SIX")
    print(f"Part 1: {inspect_first_distinct_frame(4)} \nPart 2: {inspect_first_distinct_frame(14)}")

if __name__ == "__main__":
    solve()