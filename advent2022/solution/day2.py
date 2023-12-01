from types import MappingProxyType

scores_part1 = MappingProxyType(
    {
        ("B", "X"): 1,
        ("C", "Y"): 2,
        ("A", "Z"): 3,
        ("A", "X"): 4,
        ("B", "Y"): 5,
        ("C", "Z"): 6,
        ("C", "X"): 7,
        ("A", "Y"): 8,
        ("B", "Z"): 9,
    }
)

scores_part2 = MappingProxyType(
    {
        **scores_part1,
        ("C", "X"): 2,
        ("A", "X"): 3,
        ("A", "Y"): 4,
        ("C", "Y"): 6,
        ("C", "Z"): 7,
        ("A", "Z"): 8,
    }
)

input = open('advent/resources/day_02.txt','r').read()

class Solution:
    def scores(self, puzzle_input):
        """Parse input"""
        games = []
        for game in puzzle_input.split("\n"):
            games.append(tuple(game.split(" ")))
        games.pop()
        def get_total_scores(scores):
            current_score = 0
            for game in games:
                current_score += scores.get(game)
            return current_score
        return get_total_scores(scores_part1), get_total_scores(scores_part2)
d = Solution()
d.scores(input)

def solve():
    d = Solution()
    result = d.scores(input)
    print("============")
    print("DAY TWO")
    print(f"Part 1: {result[0]} \nPart 2: {result[1]}")

if __name__ == "__main__":
    solve()