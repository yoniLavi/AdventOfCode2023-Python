#!/usr/bin/env python
from pathlib import Path
import re

import numpy as np

MY_INPUT = (Path(__file__).parent / "input.txt").read_text()


def parse_nums(num_string):
    return {int(n) for n in re.findall(r"\d+", num_string)}


def card_wins(card_nums):
    winning, yours = card_nums.strip().split("|")
    return len(parse_nums(winning) & parse_nums(yours))


def all_card_wins(input_text):
    return [card_wins(card_line.split(":")[1])
            for card_line in input_text.splitlines()]


def part1(input_text):
    return sum((2**(wins-1) if wins else 0)
               for wins in all_card_wins(input_text))


def part2(input_text):
    wins = all_card_wins(input_text)
    multiplicity = np.ones(len(wins), dtype=int)
    for card_id, card_wins in enumerate(wins):
        multiplicity[card_id + 1: card_id + card_wins + 1] += multiplicity[card_id]
    return sum(multiplicity)


print(f"{part1(MY_INPUT)=}, {part2(MY_INPUT)=}")
