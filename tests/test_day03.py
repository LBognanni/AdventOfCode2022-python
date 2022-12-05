from aoc.day03 import part1, part2

#
# --- Part One ---
#

test_input = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw""".split("\n")

def test_part1():
    assert part1.result(test_input) == 157

#
# --- Part Two ---
#

def test_part2():
    assert part2.result(None) == None
