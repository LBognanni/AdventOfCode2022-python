# Advent of Code - Day 2 - Part One

values = {
    "X": 1,
    "Y": 2,
    "Z": 3
}

win = {
    "A": "Y",
    "B": "Z",
    "C": "X"
}
draw = {
    "A": "X",
    "B": "Y",
    "C": "Z"
}

def result(input):
    score = 0

    for l in input:
        hands = l.split(" ")
        score += values[hands[1]] 

        if(win[hands[0]] == hands[1]):
            score += 6
        elif(draw[hands[0]] == hands[1]):
            score += 3
    return score

