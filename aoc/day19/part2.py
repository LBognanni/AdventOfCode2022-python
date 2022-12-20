# Advent of Code - Day 19 - Part Two
from aoc.day19 import part1

def result(input):
    sim = [part1.Simulation(part1.Blueprint(x)) for x in input[0:3]]
    return sim[0].run(32) * sim[1].run(32) * sim[2].run(32) 
