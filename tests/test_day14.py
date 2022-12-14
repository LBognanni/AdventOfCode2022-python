from aoc.day14 import part1, part2

test_input = """498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9""".split("\n")

#
# --- Part One ---
#

def test_part1():
    assert part1.result(test_input) == 24

#
# --- Part Two ---
#

def test_part2():
    assert part2.result(test_input) == 93
