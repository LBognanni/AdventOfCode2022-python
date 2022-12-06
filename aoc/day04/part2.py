import re
# Advent of Code - Day 4 - Part Two

def one_overlaps(elf1:list[int], elf2:list[int]):
    return (elf2[0] <= elf1[0] <= elf2[1]) or (elf2[0] <= elf1[1] <= elf2[1])

def line_to_elves_range(line:str):
    nums = list(map(int, re.split(r'[\- ,]', line)))
    return [[nums[0], nums[1]],[nums[2], nums[3]]]

def overlaps(elves):
    return one_overlaps(elves[0], elves[1]) or one_overlaps(elves[1], elves[0])

def result(input:list[str]):
    return sum(1 for el in filter(overlaps, map(line_to_elves_range, input)))
