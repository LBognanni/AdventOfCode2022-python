from aoc.day24 import part1, part2

test_input = """#.######
#>>.<^<#
#.<..<<#
#>v.><>#
#<^v^^>#
######.#""".split("\n")

#
# --- Part One ---
#

def test_parse():
    puzzle = part1.Puzzle(test_input)
    assert puzzle.Width == 8
    assert puzzle.Height == 6
    assert puzzle.Start == (1, 0)
    assert puzzle.End == (6,5)
    assert len(puzzle.Blizzards) == 19

def test_part1():
    assert part1.result(test_input) == 18

#
# --- Part Two ---
#

def test_part2():
    assert part2.result(test_input) == 54
