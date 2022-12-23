# Advent of Code - Day 23 - Part Two
from aoc.day23 import part1


def result(input):
    elves = set(part1.parse_input(input))

    strategies = [
        lambda x,y: [(x-1, y-1), (x, y-1), (x+1, y-1)],
        lambda x,y: [(x-1, y+1), (x, y+1), (x+1, y+1)],
        lambda x,y: [(x-1, y-1), (x-1, y), (x-1, y+1)],
        lambda x,y: [(x+1, y-1), (x+1, y), (x+1, y+1)],
    ]

    n = 0
    while n < 10000:
        (elves, moved) = part1.move(elves, strategies, n)
        if not moved:
            break 
        n+=1

    return n+1
