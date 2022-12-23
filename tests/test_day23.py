from aoc.day23 import part1, part2

test_input="""....#..
..###.#
#...#.#
.#...##
#.###..
##.#.##
.#..#..""".split("\n")

#test_input = """.....
#..##.
#..#..
#.....
#..##.
#.....
#""".split("\n")

#
# --- Part One ---
#

def test_part1():
    assert part1.result(test_input) == 110

#
# --- Part Two ---
#

def test_part2():
    assert part2.result(test_input) == 20
