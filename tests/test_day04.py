from aoc.day04 import part1, part2


test_input="""2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8""".split("\n")

#
# --- Part One ---
#

def test_part1():
    assert part1.result(test_input) == 2

#
# --- Part Two ---
#

def test_part2():
    assert part2.result(test_input) == 4
