# Advent of Code - Day 22 - Part One
from typing import Iterable
from enum import IntEnum
import re

class Facing(IntEnum):
    Right = 0
    Down = 1
    Left = 2
    Up = 3


def CalculateBoundaries(map:list[tuple[int, int, str]]) -> tuple[list[tuple[int, int]],list[tuple[int, int]]]:
    maxX = max([p[0] for p in map])
    maxY = max([p[1] for p in map])
    boundsX = []
    for y in range(maxY + 1):
        line = [p[0] for p in map if p[1] == y]
        boundsX.append((min(line), max(line)))
    boundsY = []
    for x in range(maxX + 1):
        col = [p[1] for p in map if p[0] == x]
        boundsY.append((min(col), max(col)))

    return (boundsX, boundsY)


class Puzzle:
    def __init__(self, map:list[tuple[int, int, str]], commands:str) -> None:
        self.Map = {(x,y): c for x,y,c in map}
        bounds = CalculateBoundaries(map)
        self.BoundariesX = bounds[0]
        self.BoundariesY = bounds[1]
        rgx = re.compile(r'([A-Z]+|[0-9]+)')
        self.Commands = rgx.findall(commands)
    

def parse_map(input:list[str]) -> Iterable[tuple[int, int, str]]:
    for y in range(len(input) - 2):
        for x in range(len(input[y])):
            if input[y][x] == " ":
                continue
            yield (x, y, input[y][x])

def clockWise(facing: Facing) -> Facing:
    if facing == Facing.Up:
        return Facing.Right
    elif facing == Facing.Right:
        return Facing.Down
    elif facing == Facing.Down:
        return Facing.Left
    return Facing.Up

def counterClockWise(facing: Facing) -> Facing:
    if facing == Facing.Up:
        return Facing.Left
    elif facing == Facing.Left:
        return Facing.Down
    elif facing == Facing.Down:
        return Facing.Right
    return Facing.Up

def move(pos:tuple[int, int], facing: Facing, puzzle: Puzzle) -> tuple[int, int]:
    (x,y) = pos
    if facing == Facing.Up:
        y -= 1
        if y < puzzle.BoundariesY[x][0]:
            y = puzzle.BoundariesY[x][1]
    elif facing == Facing.Left:
        x -= 1
        if x < puzzle.BoundariesX[y][0]:
            x = puzzle.BoundariesX[y][1]
    elif facing == Facing.Down:
        y += 1
        if y > puzzle.BoundariesY[x][1]:
            y = puzzle.BoundariesY[x][0]
    else:
        x += 1
        if x > puzzle.BoundariesX[y][1]:
            x = puzzle.BoundariesX[y][0]

    if puzzle.Map[(x,y)] == "#":
        return pos

    return (x, y)   

def navigate(puzzle: Puzzle) -> tuple[int, int, Facing]:
    facing = Facing.Right
    pos = (puzzle.BoundariesX[0][0], 0)
    
    for c in puzzle.Commands:
        if(c == 'L'):
            facing = counterClockWise(facing)
        elif c == 'R':
            facing = clockWise(facing)
        else:
            dist = int(c)
            for _ in range(dist):
                pos = move(pos, facing, puzzle)


    return(pos[0] + 1, pos[1] + 1, facing)


def result(input: list[str]):
    puzzle = Puzzle(list(parse_map(input)), input[len(input) - 1])
    pos = navigate(puzzle)
    return (pos[1] * 1000) + (pos[0] * 4) + pos[2]
