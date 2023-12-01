from collections import defaultdict, deque
from parse import compile

input = open('advent/resources/day_05.txt','r').read()

def parse_input(puzzle_input):
    """Parse input"""
    starting_stacks, instructions = puzzle_input.split("\n\n")
    starting_stacks = starting_stacks.split("\n")
    starting_stacks.pop(-1)  # delete stack labels
    stacks = defaultdict(deque)
    for line in starting_stacks:
        for position in range(1, len(line), 4):
            i = 1 + (position - 1) // 4
            if line[position].strip():
                stacks[i].insert(0, line[position])
    instructions_list = []
    p = compile("move {:d} from {:d} to {:d}")
    for line in instructions.split("\n"):
        instructions_list.append(tuple(p.parse(line)))
    return stacks, instructions_list

def move_crates(crate_mover_version=9000):
    parsed_input = parse_input(input)
    stacks = parsed_input[0]
    for amount, origin, destination in parsed_input[1]:
        crates_to_move = [stacks[origin].pop() for _ in range(amount)]
        if crate_mover_version == 9001:
            crates_to_move = reversed(crates_to_move)
        stacks[destination].extend(crates_to_move)
    return "".join([stacks[i][-1] for i in sorted(stacks)])

def solve():
    result = move_crates(crate_mover_version=9000)
    print("============")
    print("DAY FIVE")
    print(f"Part 1: {result} \nPart 2: {move_crates(crate_mover_version=9001)}")

if __name__ == "__main__":
    solve()