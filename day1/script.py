#!/usr/bin/env python
from pathlib import Path
import re

DIGITS = {
    "one": 1, "two": 2, "three": 3,
    "four": 4, "five": 5, "six": 6,
    "seven": 7, "eight": 8, "nine": 9,
}

PART1_DIGITS_RE = re.compile("\\d")
PART2_DIGITS_RE = re.compile(f"(\\d|{'|'.join(DIGITS)})")
PART2_REVERSE_DIGITS_RE = re.compile(f"(\\d|{'|'.join(d[::-1] for d in DIGITS)})")

MY_INPUT = (Path(__file__).parent / "input.txt").read_text()


def digit(regex, line, reversed=False):
    digit = regex.search(line[::-1] if reversed else line).group()
    return DIGITS.get(digit[::-1] if reversed else digit) or int(digit)


def calibration(text, forward_re, reverse_re):
    return sum(10 * digit(forward_re, l) + digit(reverse_re, l, reversed=True)
               for l in text.splitlines())


part1 = calibration(MY_INPUT, PART1_DIGITS_RE, PART1_DIGITS_RE)
part2 = calibration(MY_INPUT, PART2_DIGITS_RE, PART2_REVERSE_DIGITS_RE)
print(f"{part1=}, {part2=}")
