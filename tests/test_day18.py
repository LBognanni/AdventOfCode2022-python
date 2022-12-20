from aoc.day18 import part1, part2

test_input = """2,2,2
1,2,2
3,2,2
2,1,2
2,3,2
2,2,1
2,2,3
2,2,4
2,2,6
1,2,5
3,2,5
2,1,5
2,3,5""".split("\n")

#
# --- Part One ---
#

def test_part1():
    assert part1.result(test_input) == 64

#
# --- Part Two ---
#

def test_part2():
    assert part2.result(test_input) == 58
