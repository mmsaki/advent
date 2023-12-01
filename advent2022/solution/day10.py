from utils import convert_array_6

input = open("advent/resources/day_10.txt", "r").read()

def parse_input(puzzle_input):
    """Parse input"""
    return (
        [line.strip() for line in puzzle_input.split("\n")],
        [],
        [[" " for x in range(40)] for y in range(6)],
    )

def run_program():
    instructions, signal_strengths, sprite = parse_input(input)
    cycle, value = 0, 1

    for instruction in instructions:
        command, steps = (
            split_instruction
            if len(split_instruction := instruction.split()) == 2
            else (split_instruction[0], 0)
        )
        cycles = {"noop": 1, "addx": 2}.get(command, 0)
        for _ in range(cycles):
            if (x := cycle % 40) in (value - 1, value, value + 1):
                sprite[cycle // 40][x] = "#"
            cycle += 1
            if cycle in (20, 60, 100, 140, 180, 220):
                signal_strengths.append(value * cycle)
        if command == "addx":
            value += int(steps)

    solved = True
    sprite_ = ["".join(pixel) for pixel in sprite]
    try:
        sprite_ = convert_array_6(sprite_, empty_pixel=" ")
    except KeyError:
        pass
    part1_solution, part2_solution = (
        sum(signal_strengths),
        sprite_,
    )
    
    def part1():
        """Solve part 1"""
        if not solved:
            run_program()
        return part1_solution

    def part2():
        """Solve part 2"""
        if not solved:
            run_program()
        return part2_solution
    
    return part1(), part2()

def solve():
    """Solve the puzzle"""
    print("============")
    print(f"Day TEN")
    part1, part2 = run_program()
    print(f"Part 1: {part1} \nPart 2: {part2}")


if __name__ == "__main__":
    solve()