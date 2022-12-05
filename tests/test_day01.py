from aoc.day01 import part1, part2

#
# --- Part One ---
#

test_input = """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000"""

def test_part1():
    maxCalories = part1.result(test_input.split("\n"))
    assert maxCalories == 24000

#
# --- Part Two ---
#

def test_part2():
    assert part2.result(test_input.split("\n")) == 45000
