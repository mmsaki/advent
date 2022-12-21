input = open('advent/resources/day_04.txt','r').read()

def solution(puzzle_input):
    """Parse input"""
    expanded_section_list = []
    for line in puzzle_input.split("\n"):
        sections = []
        for elf in line.split(","):
            lower_end, upper_end = tuple(map(int, elf.split("-")))
            sections.append(set(range(lower_end, upper_end + 1)))
        expanded_section_list.append(sections)
    
    def _count_overlaps(sections):
        fully_overlaps = overlaps = 0
        for section in sections:
            if intersect := set.intersection(*section):
                overlaps += 1
                if intersect in section:
                    fully_overlaps += 1
        return fully_overlaps, overlaps
    return _count_overlaps(expanded_section_list)

def solve():
    result = solution(input)
    print("============")
    print("DAY FOUR")
    print(f"Part 1: {result[0]} \nPart 2: {result[1]}")


if __name__ == "__main__":
    solve()