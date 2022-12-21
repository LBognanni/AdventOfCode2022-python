from aoc.day20 import part1
# Advent of Code - Day 20 - Part Two

def result(input): 
    print("")
    numbers = part1.move_numbers(list(map(lambda x: int(x) * 811589153, input)), 10)
    idx = numbers.index(0)

    return  numbers[(idx + 1000) % len(numbers)] + \
            numbers[(idx + 2000) % len(numbers)] + \
            numbers[(idx + 3000) % len(numbers)]
