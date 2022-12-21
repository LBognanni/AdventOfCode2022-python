from aoc.day20 import part1, part2

test_input = """1
2
-3
3
-2
0
4""".split("\n")

#
# --- Part One ---
#

def test_move_numbers():
    assert part1.move_numbers([1, 2, -3, 3, -2, 0, 4]) == [1, 2, -3, 4, 0, 3, -2]

def test_part1():
    assert part1.result(test_input) == 3

#
# --- Part Two ---
#

def test_part2():
    assert part2.result(None) == None
