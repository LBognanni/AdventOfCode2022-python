# Advent of Code - Day 3 - Part Two
from aoc.day03 import part1

def chunk_list (list, x):
    return [list[i:i+x] for i in range(0, len(list), x)]

def find_shared(list1, list2, list3):
    for c in list1:
        if c in list2 and c in list3:
            return c
    return None

def result(input:list[str]):
    return sum(list(map(lambda group: part1.score(find_shared(group[0], group[1], group[2])), chunk_list(input, 3))))
