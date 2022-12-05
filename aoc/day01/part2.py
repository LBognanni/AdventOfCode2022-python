# Advent of Code - Day 1 - Part Two

def topThree(arr):
    return sorted(arr, reverse=True)[0:3]


def result(input):
    elfs = []
    current = 0
    for l in input:
        if l == "":
            elfs.append(current)
            current = 0
        else:
            current = current + int(l)
    if (current > 0):
        elfs.append(current)
    return sum(topThree(elfs))
