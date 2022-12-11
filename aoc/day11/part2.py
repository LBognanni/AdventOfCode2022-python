from aoc.day11 import part1
from functools import reduce 
# Advent of Code - Day 11 - Part Two


def run(monkey:part1.Monkey, monkeys:list[part1.Monkey], magic_number):
    for orig in monkey.items:
        item = (monkey.operation.run(orig))
        throw_to =  monkey.monkey_true if(item % monkey.divide_by == 0) else monkey.monkey_false
        monkeys[throw_to].items.append(item % magic_number)
        monkey.times_inspected+=1
    monkey.items = []


def result(input):

    monkeys = part1.parse_input(input)
    rounds = 10000

    magic_number = reduce(lambda a,b: a * b, set(map(lambda m: m.divide_by, monkeys)), 1)

    for _ in range(0, rounds):
        for monkey in monkeys:
            run(monkey,monkeys, magic_number)
        pass

    values = sorted(map(lambda m: m.times_inspected, monkeys), reverse=True)

    return values[0] * values[1]
