from aoc.day21 import part1, part2

test_input = """root: pppw + sjmn
dbpl: 5
cczh: sllz + lgvd
zczc: 2
ptdq: humn - dvpt
dvpt: 3
lfqf: 4
humn: 5
ljgn: 2
sjmn: drzm * dbpl
sllz: 4
pppw: cczh / lfqf
lgvd: ljgn * ptdq
drzm: hmdt - zczc
hmdt: 32""".split("\n")

#
# --- Part One ---
#

def test_part1():
    assert part1.result(test_input) == 152

#
# --- Part Two ---
#

def test_part2():
    assert part2.result(None) == None
