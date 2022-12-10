from aoc.day09 import part1, part2

#
# --- Part One ---
#

test_input = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2""".split("\n")

def test_part1():
    assert part1.result(test_input) == 13

#
# --- Part Two ---
#

def test_part2():
    assert part2.result(None) == None
