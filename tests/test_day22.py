from aoc.day22 import part1, part2

test_input = """        ...#
        .#..
        #...
        ....
...#.......#
........#...
..#....#....
..........#.
        ...#....
        .....#..
        .#......
        ......#.

10R5L5R10L4R5L5""".split("\n")

#
# --- Part One ---
#

def test_part1():
    assert part1.result(test_input) == 6032

#
# --- Part Two ---
#

def test_part2():
    assert part2.result(test_input) == 5031
