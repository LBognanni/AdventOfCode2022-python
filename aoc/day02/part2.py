# Advent of Code - Day 2 - Part Two

values = {
    "R": 1,
    "P": 2,
    "S": 3
}

strategy = {
    "X": {
        "A": "S",
        "B": "R",
        "C": "P",
        "Score": 0
    },
    "Y": {
        "A": "R",
        "B": "P",
        "C": "S",
        "Score": 3
    },
    "Z": {
        "A": "P",
        "B": "S",
        "C": "R",
        "Score": 6
    }
}

def result(input):
    score = 0
    for l in input:
        hands = l.split(" ")
        score += strategy[hands[1]]["Score"] + values[strategy[hands[1]][hands[0]]]
    return score
