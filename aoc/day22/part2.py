# Advent of Code - Day 22 - Part Two
from aoc.day22.part1 import Puzzle, parse_map, clockWise, counterClockWise, Facing
from enum import IntEnum
import re

class Side(IntEnum):
    Front = 0
    Bottom = 1
    Left = 2
    Right = 3
    Back = 4
    Top = 5




class CubeFace:
    def __init__(self, range:tuple[tuple[int, int], tuple[int, int]], side: Side) -> None:
        self.Range = range
        self.Side = side
        self.Up = None
        self.Down = None
        self.Left = None
        self.Right = None




def result(input):
    puzzle = Puzzle(list(parse_map(input)), input[len(input) - 1])
    faces:list[CubeFace] = []
    if len(input < 40):
        faces = {
            Side.Front: CubeFace(((8, 0), (12, 4)), Side.Front),
            Side.Left: CubeFace(((4, 4), (8, 8)), Side.Left),
            Side.Bottom: CubeFace(((8, 4), (12, 8)), Side.Bottom),
            Side.Back: CubeFace(((4, 8), (8, 12)), Side.Back),
            Side.Top: CubeFace(((0, 12), (4, 12)), Side.Top),
            Side.Right: CubeFace(((4, 12), (8, 12)), Side.Right),
        }
        faces[Side.Front].Up = (faces[Side.Top], lambda x,y: (x - 8, 11, Facing.Up))
        faces[Side.Front].Down = (faces[Side.Bottom], lambda x,y: (x, y, Facing.Down))
        faces[Side.Front].Left = (faces[Side.Left], lambda x,y: (y + 4, 4, Facing.Down))
        faces[Side.Front].Right = (faces[Side.Right], lambda x,y: (y + 4, 11, Facing.Up))
                
        faces[Side.Bottom].Up = (faces[Side.Front], lambda x,y: (x, y, Facing.Up))
        faces[Side.Bottom].Down = (faces[Side.Back], lambda x,y: (7, x, Facing.Left))
        faces[Side.Bottom].Left = (faces[Side.Left], lambda x,y: (y, y, Facing.Down))
        faces[Side.Bottom].Right = (faces[Side.Right], lambda x,y: (7, 12-(y-4), Facing.Up))
        
        


    return None
