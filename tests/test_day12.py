from aoc.day12 import part1, part2

#
# --- Part One ---
#

test_input = """Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi""".split("\n")

def test_part1():
    assert part1.result(test_input) == 31

#
# --- Part Two ---
#

def test_part2():
    assert part2.result(test_input) == 29
