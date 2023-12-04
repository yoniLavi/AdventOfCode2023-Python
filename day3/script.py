#!/usr/bin/env python
from collections import defaultdict
from pathlib import Path
import re

import numpy as np

JUST_ASTERISK = np.array(["*"])
ALL_SYMBOLS = np.array(list("#$%&*+-/=@"))

MY_INPUT = (Path(__file__).parent / "input.txt").read_text()


def neighbors(grid, row, start_col, end_col):
    return grid[max(0, row - 1) : row + 2, max(0, start_col - 1) : end_col + 2]


def match_in_neighborhood(grid, row, start_col, end_col, symbols):
    match = np.where(np.isin(neighbors(grid, row, start_col, end_col), symbols))
    if not match[0].size:
        return None
    match_row = match[0][0] + max(0, row - 1)
    match_col = match[1][0] + max(0, start_col - 1)
    return match_row, match_col


def extract_numbers_in_row(grid, line, row, symbols):
    for match in re.finditer(r"\d+", line):
        symbol_pos = match_in_neighborhood(grid, row, match.start(), match.end() - 1, symbols)
        if symbol_pos:
            yield int(match.group()), symbol_pos


def extract_numbers_in_grid_next_to_symbol(grid_text):
    grid = np.array([list(line) for line in grid_text.splitlines()])
    for row, line in enumerate(grid_text.splitlines()):
        for num, _ in extract_numbers_in_row(grid, line, row, ALL_SYMBOLS):
            yield num


def part1(text):
    return sum(extract_numbers_in_grid_next_to_symbol(text))


def extract_products_in_grid(grid_text):
    grid = np.array([list(line) for line in grid_text.splitlines()])
    numbers_next_to_asterisk = defaultdict(list)
    for row, line in enumerate(grid_text.splitlines()):
        for num, asterisk_pos in extract_numbers_in_row(grid, line, row, JUST_ASTERISK):
            numbers_next_to_asterisk[asterisk_pos].append(num)

    for numbers in numbers_next_to_asterisk.values():
        if len(numbers) == 2:
            yield np.prod(numbers)


def part2(text):
    return sum(extract_products_in_grid(text))


print(f"{part1(MY_INPUT)=}, {part2(MY_INPUT)=}")
