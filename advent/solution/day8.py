# aoc_day_08.py
from copy import deepcopy

input = open("advent/resources/day_08.txt", "r").read()

def solution(puzzle_input):
    """Parse input"""
    tree_map = tuple(
        tuple(int(height) for height in line)
        for line in puzzle_input.split("\n")
    )
    tree_visibility_mask = []
    for line_index, line in enumerate(tree_map):
        tree_visibility_mask.append([])
        for tree_index, tree in enumerate(line):
            if line_index in (0, len(tree_map) - 1) or tree_index in (
                0,
                len(line) - 1,
            ):
                tree_visibility_mask[line_index].append(1)
            else:
                tree_visibility_mask[line_index].append(0)
    return score_trees(tree_map, tree_visibility_mask)

def is_left_smaller(tree_map, line_index, column_index):
    return (
        max(tree_map[line_index][0:column_index])
        < tree_map[line_index][column_index]
    )

def is_right_smaller(tree_map, line_index, column_index):
    return (
        max(tree_map[line_index][column_index + 1 : len(tree_map)])
        < tree_map[line_index][column_index]
    )

def is_upper_smaller(tree_map, line_index, column_index):
    upper_heights = [
        tree_map[index][column_index] for index in range(line_index)
    ]
    return max(upper_heights) < tree_map[line_index][column_index]

def is_lower_smaller(tree_map, line_index, column_index):
    lower_heights = [
        tree_map[index][column_index]
        for index in range(line_index + 1, len(tree_map))
    ]
    return max(lower_heights) < tree_map[line_index][column_index]

def get_left_score(tree_map, line_index, column_index):
    current_height = tree_map[line_index][column_index]
    score = 0
    if not column_index:
        return 0
    for height in reversed(tree_map[line_index][:column_index]):
        score += 1
        if height >= current_height:
            break
    return score

def get_right_score(tree_map, line_index, column_index):
    current_height = tree_map[line_index][column_index]
    score = 0
    if column_index == len(tree_map[line_index]):
        return 0
    for height in tree_map[line_index][column_index + 1 :]:
        score += 1
        if height >= current_height:
            break
    return score

def get_lower_score(tree_map, line_index, column_index):
    current_height = tree_map[line_index][column_index]
    score = 0
    if line_index == len(tree_map) - 1:
        return 0
    for height in tree_map[line_index + 1 :]:
        height = height[column_index]
        score += 1
        if height >= current_height:
            break
    return score

def get_upper_score(tree_map, line_index, column_index):
    current_height = tree_map[line_index][column_index]
    score = 0
    if not line_index:
        return 0
    for height in reversed(tree_map[:line_index]):
        height = height[column_index]
        score += 1
        if height >= current_height:
            break
    return score

def score_trees(tree_map, scoring_mask):
    tree_visibility_mask, tree_scores = deepcopy(scoring_mask), deepcopy(
        scoring_mask
    )
    seen_trees_counter = 0
    for line_index, line in enumerate(tree_map):
        for column_index, tree in enumerate(line):
            if tree_visibility_mask[line_index][column_index] == 1:
                seen_trees_counter += 1
            elif (
                is_left_smaller(tree_map, line_index, column_index)
                or is_right_smaller(
                    tree_map, line_index, column_index
                )
                or is_upper_smaller(
                    tree_map, line_index, column_index
                )
                or is_lower_smaller(
                    tree_map, line_index, column_index
                )
            ):
                tree_visibility_mask[line_index][column_index] = 1
                seen_trees_counter += 1
            tree_scores[line_index][column_index] = (
                get_upper_score(tree_map, line_index, column_index)
                * get_left_score(tree_map, line_index, column_index)
                * get_lower_score(tree_map, line_index, column_index)
                * get_right_score(tree_map, line_index, column_index)
            )
        tree_scores[line_index] = max(tree_scores[line_index])
    return seen_trees_counter, max(tree_scores)

def solve():
    result = solution(input)
    print("===========")
    print("DAY EIGHT")
    print(f"Part 1: {result[0]} \nPart 2: {result[1]}")


if __name__ == "__main__":
    solve()
    