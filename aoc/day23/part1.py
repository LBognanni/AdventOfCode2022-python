# Advent of Code - Day 23 - Part One
from typing import Iterable

def parse_input(input:list[str]) -> Iterable[tuple[int, int]]:
    for y in range(len(input)):
        line = input[y]
        for x in range(len(line)):
            if(line[x] == "#"):
                yield (x, y)

def move(elves:set[tuple[int, int]], strategies:list, start:int) -> tuple[set[tuple[int, int]], bool]:
    newMoves = []
    someone_moved = False
    final_moves = set()

    for x,y in elves:
        newPos = (x,y)

        neighbours = False
        for xx in range(x-1, x+2):
            for yy in range(y-1, y+2):
                if xx == x and yy == y:
                    continue
                if (xx, yy) in elves:
                    neighbours = True
                    break
            if neighbours: break

        if neighbours:
            for i in range(0, 4):
                found = True
                strategy:list[tuple[int, int]] = strategies[(start + i) % 4](x,y)
                for p in strategy:
                    if p in elves:
                        found = False
                        break
                if found:
                    newPos = strategy[1]
                    break

            newMoves.append(((x,y), newPos))
        else:
            final_moves.add(newPos)
    
    for oldPos, newPos in newMoves:
        others = [1 for p in newMoves if p[1] == newPos]
        if len(others) == 1:
            someone_moved = True
            final_moves.add(newPos)
        else:
            final_moves.add(oldPos)

    return (final_moves, someone_moved)

def print_elves(elves:list[tuple[int, int]]):
    Xs = [p[0] for p in elves]
    Ys = [p[1] for p in elves]
    for y in range(min(Ys) - 1, max(Ys) + 1):
        for x in range(min(Xs) - 1, max(Xs) + 1):
            if (x, y) in elves:
                print('#', end="")
            else:
                print(".", end="")
        print("")

def result(input):
    elves = set(parse_input(input))

    strategies = [
        lambda x,y: [(x-1, y-1), (x, y-1), (x+1, y-1)],
        lambda x,y: [(x-1, y+1), (x, y+1), (x+1, y+1)],
        lambda x,y: [(x-1, y-1), (x-1, y), (x-1, y+1)],
        lambda x,y: [(x+1, y-1), (x+1, y), (x+1, y+1)]
    ]

    #print("\nSTART ")
    #print_elves(elves)
    #print("")

    for i in range(10):
        (elves, _) = move(elves, strategies, i)
        #print("ROUND ", i)
        #print_elves(elves)
        #print("")
    
    Xs = [p[0] for p in elves]
    Ys = [p[1] for p in elves]

    return ((max(Xs) + 1) - min(Xs)) * ((max(Ys) + 1) - min(Ys)) - len(elves)
