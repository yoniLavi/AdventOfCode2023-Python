#!/usr/bin/env python
from collections import defaultdict
from pathlib import Path

MY_INPUT = (Path(__file__).parent / "input.txt").read_text()

MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14

class Game:
    def __init__(self, text):
        gid, reveals = text.split(":")
        self.gid = int(gid.split()[-1])
        self.cubes = defaultdict(int)
        for reveal in reveals.split(";"):
            self.process_reveal(reveal)

    def process_reveal(self, reveal):
        for cube_text in reveal.split(","):
            count, color = cube_text.strip().split()
            self.cubes[color] = max(self.cubes[color], int(count))

    def value(self):
        valid = all([self.cubes["red"] <= MAX_RED,
                     self.cubes["blue"] <= MAX_BLUE,
                     self.cubes["green"] <= MAX_GREEN])
        return self.gid if valid else 0

    def power(self):
        return self.cubes["red"] * self.cubes["blue"] * self.cubes["green"]


def part1(text):
    return sum(Game(game).value() for game in text.splitlines())


def part2(text):
    return sum(Game(game).power() for game in text.splitlines())


print(part1(MY_INPUT))
print(part2(MY_INPUT))
