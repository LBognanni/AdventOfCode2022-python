from aoc.day06 import part1, part2

#
# --- Part One ---
#
test_input = ["bvwbjplbgvbhsrlpgdmjqwftvncz"]

def test_part1():
    assert part1.result(test_input) == 5
    assert part1.result(["nppdvjthqldpwncqszvftbrmjlhg"]) == 6
    assert part1.result(["nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"]) == 10
    assert part1.result(["zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"]) == 11

#
# --- Part Two ---
#

def test_part2():
    assert part2.result(["mjqjpqmgbljsphdztnvjfqwrcgsmlb"]) == 19
    assert part2.result(["bvwbjplbgvbhsrlpgdmjqwftvncz"]) == 23
    assert part2.result(["nppdvjthqldpwncqszvftbrmjlhg"]) == 23
    assert part2.result(["nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"]) == 29
