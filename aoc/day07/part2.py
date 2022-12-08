from aoc.day07 import part1
# Advent of Code - Day 7 - Part Two

def result(input):
    total_space = 70000000
    folders = part1.parse_folders(input)
    free_space = total_space - folders["/"]["size"]
    space_to_free = 30000000 - free_space

    return sorted(filter(lambda x: x>=space_to_free, map(lambda x: x["size"], folders.values())))[0]
