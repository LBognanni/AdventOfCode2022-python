from aoc.day19 import part1, part2


test_input="""Blueprint 1: Each ore robot costs 4 ore. Each clay robot costs 2 ore. Each obsidian robot costs 3 ore and 14 clay. Each geode robot costs 2 ore and 7 obsidian.
Blueprint 2: Each ore robot costs 2 ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 8 clay. Each geode robot costs 3 ore and 12 obsidian.""".split("\n")

#
# --- Part One ---
#

def test_parse():
    bp = part1.Blueprint(test_input[0])
    assert bp.Id == 1
    assert bp.Costs["ore"] == [("ore", 4)]
    assert bp.Costs["clay"] == [("ore", 2)]
    assert bp.Costs["obsidian"] == [("ore", 3), ("clay", 14)] 


def test_part1():
    #assert part1.result([test_input[0]]) == 9
    #assert part1.result([test_input[1]]) == 12
    assert part1.result(test_input) == 33

#
# --- Part Two ---
#

def test_part2():
    assert part2.result(None) == None
