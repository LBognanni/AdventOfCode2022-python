from aoc.day08 import part1, part2

test_input = """30373
25512
65332
33549
35390""".split("\n")

#
# --- Part One ---
#

def test_part1():
    assert part1.result(test_input) == 21

#
# --- Part Two ---
#

def test_part2():
    assert part2.result(None) == None
