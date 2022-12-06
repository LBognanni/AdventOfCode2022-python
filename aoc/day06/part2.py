# Advent of Code - Day 6 - Part Two
from aoc.day06 import part1

def result(input):
    str = input[0]
    for i in range(14, len(str)):
        if(part1.uniq(str[i-14:i])):
            return i
    return None
