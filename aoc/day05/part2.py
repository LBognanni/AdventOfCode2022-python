# Advent of Code - Day 5 - Part Two
from aoc.day05 import part1

def result(input):
    (stacks, movements) = part1.parse(input)

    for (howMany, fromPos, toPos) in movements:
        els = stacks[fromPos][:howMany]
        stacks[toPos] = els + stacks[toPos]
        stacks[fromPos] = stacks[fromPos][howMany:]

    return "".join(map(lambda x:x[0], stacks.values()))
