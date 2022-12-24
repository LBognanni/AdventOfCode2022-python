# Advent of Code - Day 24 - Part One
from enum import Enum

class Direction(Enum):
    Up = 1
    Right = 2
    Down = 3
    Left = 4

def parseDirection(c) -> Direction:
    if c == ">": return Direction.Right
    if c == "<": return Direction.Left
    if c == "^": return Direction.Up
    if c == "v": return Direction.Down
    raise Exception("wtf")

def printBlizzard(c:Direction) -> str:
    if c == Direction.Right: return ">"
    if c == Direction.Left: return "<"
    if c == Direction.Up: return "^"
    if c == Direction.Down: return "v"
    raise Exception("wtf")

directionStrategy = {
    Direction.Up: lambda x,y,w,h: (x, y-1 if y > 1 else h - 2, Direction.Up),
    Direction.Right: lambda x,y,w,h: (x + 1 if x < (w-2) else 1, y, Direction.Right),
    Direction.Down: lambda x,y,w,h: (x, y + 1 if y < (h-2) else 1, Direction.Down),
    Direction.Left: lambda x,y,w,h: (x-1 if x > 1 else w - 2, y, Direction.Left),
}

class Puzzle:
    def __init__(self, input:list[str]) -> None:
        self.Width = len(input[0])
        self.Height = len(input)
        self.Map:list[list[bool]] = []
        self.Blizzards = []
        self.Start:tuple[int, int] = None
        self.End:tuple[int, int] = None
        self.Trips:set[tuple[int, int]] = set()

        for y in range(self.Height):
            line = []
            for x in range(self.Width):
                c = input[y][x]
                if(c == "."):
                    line.append(False)
                    if y == 0 and self.Start == None:
                        self.Start = (x,y)
                    elif y == len(input) -1 and self.End == None:
                        self.End = (x,y)
                else:
                    line.append(True)
                    if c != "#":
                        self.Blizzards.append((x,y,parseDirection(c)))
            self.Map.append(line)
        
        self.Trips.add(self.Start)

    def Tick(self, goal:tuple[int, int]):
        for y in range(1, self.Height - 1):
            for x in range(1, self.Width - 1):
                self.Map[y][x] = False

        newBlizzards = []
        for x,y,d in self.Blizzards:
            b = directionStrategy[d](x,y,self.Width, self.Height)
            self.Map[b[1]][b[0]] = True
            newBlizzards.append(b)
        self.Blizzards = newBlizzards

        newTrips = set()
        for (x,y) in self.Trips:

            if((x,y) == goal):
                return True

            if y < self.Height and (x,y) != self.End and not self.Map[y+1][x]:
                newTrips.add((x, y+1))
            if not self.Map[y][x+1]:
                newTrips.add((x+1, y))
            if not self.Map[y][x-1]:
                newTrips.add((x-1, y))
            if y > 0 and not self.Map[y-1][x]:
                newTrips.add((x, y-1))
            if not self.Map[y][x]:
                newTrips.add((x,y))

        self.Trips = newTrips
        
        return False
        
    def print_map(self):
        for y in range(self.Height):
            for x in range(self.Width):
                if (x,y) in self.Trips:
                    print("o", end="")
                else:
                    blz = [b for b in self.Blizzards if b[0] == x and b[1] ==y]
                    if len(blz) == 0:
                        if self.Map[y][x]:
                            print("#", end="")
                        else:
                            print(".", end="")
                    elif len(blz) == 1:
                        print(printBlizzard(blz[0][2]), end="")
                    else:
                        print(len(blz), end="")
            print("")


def result(input:list[str]):
    p = Puzzle(input)
    for i in range(20000):
        if p.Tick(p.End):
            return i
        #print(i)
        #p.print_map()
    return -1
