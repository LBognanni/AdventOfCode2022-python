# Advent of Code - Day 3 - Part One

def score(letter):
    asc = ord(letter)
    if(asc >= ord("a")):
        return asc - ord("a") + 1
    return asc - ord("A") + 27

def findShared(iterate:list[str], find:list[str]):
    result = []
    for c in iterate:
        if c in find:
            if not c in result:
                result.append(c)
    return result

def sumScore(items:list[str]):
    return sum(list(map(score, items)))

def result(input):
    score = 0
    line:str
    for line in input:
        c1 = line[:len(line)//2]
        c2 = line[len(line)//2:]
        shared = findShared(c1, c2)
        score += sumScore(shared)
        
    return score
