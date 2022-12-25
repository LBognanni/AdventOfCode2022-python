from aoc.day25 import part1, part2

test_input = """1=-0-2
12111
2=0=
21
2=01
111
20012
112
1=-1=
1-12
12
1=
122""".split("\n")

def test_snafuToDec():
    assert part1.snafuToDec('1=-0-2') == 1747
    assert part1.snafuToDec('1=-0-2') == 1747
    assert part1.snafuToDec('12111') == 906
    assert part1.snafuToDec('2=0=')  == 198
    assert part1.snafuToDec('21')  == 11
    assert part1.snafuToDec('2=01') == 201
    assert part1.snafuToDec('111')  == 31
    assert part1.snafuToDec('20012') == 1257
    assert part1.snafuToDec('112')  == 32
    assert part1.snafuToDec('1=-1=')  == 353
    assert part1.snafuToDec('1-12') == 107
    assert part1.snafuToDec('12')   == 7
    assert part1.snafuToDec('1=')    == 3
    assert part1.snafuToDec('122')  == 37

def test_decToSnafu():
    assert part1.decToSnafu(1) == "1"
    assert part1.decToSnafu(2) == "2"
    assert part1.decToSnafu(3) == "1="
    assert part1.decToSnafu(4) == "1-"
    assert part1.decToSnafu(5) == "10"
    assert part1.decToSnafu(6) == "11"
    assert part1.decToSnafu(7) == "12"
    assert part1.decToSnafu(8) == "2="
    assert part1.decToSnafu(9) == "2-"
    assert part1.decToSnafu(10) == "20"
    assert part1.decToSnafu(15) == "1=0"
    assert part1.decToSnafu(20) == "1-0"
    assert part1.decToSnafu(2022) == "1=11-2"
    assert part1.decToSnafu(12345) == "1-0---0"
    assert part1.decToSnafu(314159265) == "1121-1110-1=0"
#
# --- Part One ---
#

def test_part1():
    assert part1.result(test_input) == '2=-1=0'

#
# --- Part Two ---
#

def test_part2():
    assert part2.result(None) == None
