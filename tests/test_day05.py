from aoc.day05 import part1, part2


test_input="""    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2""".split("\n")

#
# --- Part One ---
#

def test_part1():
    assert part1.result(test_input) == "CMZ"

#
# --- Part Two ---
#

def test_part2():
    assert part2.result(test_input) == "MCD"
