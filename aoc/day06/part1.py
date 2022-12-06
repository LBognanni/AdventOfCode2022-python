# Advent of Code - Day 6 - Part One

def uniq(str:str):
    return len(set(str)) == len(str)

def result(input):
    str = input[0]
    for i in range(4, len(str)):
        if(uniq(str[i-4:i])):
            return i
    return None

