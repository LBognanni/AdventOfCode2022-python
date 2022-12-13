# Advent of Code - Day 13 - Part Two
from aoc.day13 import part1
from functools import cmp_to_key

def result(input:list[str]):

    if not "[[6]]" in input:
        input.append("[[6]]")
    if not "[[2]]" in input:
        input.append("[[2]]")

    allthethings = list(map(part1.parse_line, filter(lambda l: l!="", input)))

    things_sorted = sorted(allthethings, key= cmp_to_key(part1.compare_things))

    return (things_sorted.index([[6]]) + 1) * (things_sorted.index([[2]]) + 1)
