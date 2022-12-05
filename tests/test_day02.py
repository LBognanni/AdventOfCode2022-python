from aoc.day02 import part1, part2

#
# --- Part One ---
#
test_input = """A Y
B X
C Z""".split("\n")

def test_part1():
    assert part1.result(test_input) == 15

#
# --- Part Two ---
#

def test_part2():
    assert part2.result(None) == None
