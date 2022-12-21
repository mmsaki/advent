from aocd import get_data
from sympy import Eq, solve, simplify, Symbol

input = get_data(day=21, year=2022)

class Solution:
    def __init__(self, input):
        self.input = input
        self.solved = {}
        self.solved2 = {}
        self.unsolved = {}

    def operators(self):
        for i in self.input.splitlines():
            name, num = i.split(": ")
            if name == "humn":
                self.solved[name] = num
                self.solved2[name] = 'x'
            elif num.isdigit():
                self.solved[name] = int(num)
                self.solved2[name] = int(num)
            else:
                self.unsolved[name] = num

    def part1(self):
        for monkey, arg in self.unsolved.items():
            if monkey == "root":
                left, op, right = arg.split()
                return eval(f"{self.recurse(left)} {op} ({eval(self.recurse(right))})")
    
    def recurse(self, unsolved_):
        if unsolved_ in self.solved.keys():
            return f"{self.solved[unsolved_]}"
        else:
            left, op, right = self.unsolved[unsolved_].split()
            return f"({self.recurse(left)} {op} {self.recurse(right)})"

    def part2(self):
        for monkey, arg in self.unsolved.items():
            if monkey == "root":
                left, op, right = arg.split()
                x = self.recurse2(left)
                y = eval(self.recurse2(right))
                expr = Eq(simplify(x), y)
                return solve(expr, Symbol('x'))
    
    def recurse2(self, unsolved_):
        if unsolved_ in self.solved2.keys():
            return f"{self.solved2[unsolved_]}"
        else:
            left, op, right = self.unsolved[unsolved_].split()
            return f"({self.recurse2(left)} {op} {self.recurse2(right)})"

    


p = Solution(input)
p.operators()

print(f"Part 1: {p.part1()} Part 2: {p.part2()[0]}")