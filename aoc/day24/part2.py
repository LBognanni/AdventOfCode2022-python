# Advent of Code - Day 24 - Part Two
from aoc.day24.part1 import Puzzle


def result(input):

    n = 0    
    p = Puzzle(input)
    trips = [(p.Start, p.End), (p.End, p.Start), (p.Start, p.End)]
    add = 0
    for start, end in trips:

        p.Trips = set([start])

        for i in range(20000):
            if p.Tick(end):
                print(i)
                n += i + add
                add = 1     # I'm off by one and I don't understand why
                break

        
    return n
