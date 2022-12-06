import re
# Advent of Code - Day 4 - Part One


def one_fully_contains(elf1:list[int], elf2:list[int]):
    return (elf1[0] >= elf2[0] and elf1[1]<=elf2[1])

def line_to_elves_range(line:str):
    nums = list(map(int, re.split(r'[\- ,]', line)))
    return [[nums[0], nums[1]],[nums[2], nums[3]]]

def fully_contains(elves):
    return one_fully_contains(elves[0], elves[1]) or one_fully_contains(elves[1], elves[0])

def result(input:list[str]):
    return sum(1 for el in filter(fully_contains, map(line_to_elves_range, input)))

