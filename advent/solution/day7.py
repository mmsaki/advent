from collections import defaultdict
import sys

input = open('advent/resources/day_07.txt','r').read()

def solution(puzzle_input):
        """Parse input"""
        return build_directory_tree(
            tuple(line.strip() for line in puzzle_input.split("\n"))
        )
def build_directory_tree(history):
    total_sizes, current_position, folder_stack = (
        defaultdict(lambda: 0),
        1,
        [""],
    )
    while current_position < len(history):
        current_row = history[current_position]
        match current_row.split():
            case ["$", "cd", ".."]:
                folder_stack.pop()
                current_position += 1
            case ["$", "cd", folder]:
                folder_stack.append(folder)
                current_position += 1
            case ["$", "ls"]:
                new_position = current_position + 1
                while new_position < len(history):
                    command = history[new_position]
                    if command.startswith("$"):
                        break
                    elif not command.startswith("dir"):
                        size = int(command.split()[0])
                        for index in range(len(folder_stack)):
                            total_sizes[
                                "/".join(folder_stack[: index + 1])
                            ] += size
                    new_position += 1
                current_position = new_position
    return total_sizes


def solve():
    result = solution(input)
    def part2():
        unused_space = 70_000_000 - result[""]
        return min(size for size in result.values() if unused_space + size >= 30_000_000)
    print("============")
    print("DAY SEVEN")
    print(f"Part 1: {sum(size for size in result.values() if size <= 100_000)} \nPart 2: {part2()}")


if __name__ == "__main__":
    solve()