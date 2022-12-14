from functools import reduce

# Advent of Code - Day 14 - Part One

def parsePoint(pt:str) -> list[int]:
    return [int(coord) for coord in pt.split(",")]

def parseLine(line:str) -> list[list[int]]:
    return [parsePoint(pt) for pt in line.split(" -> ")]

def expandLines(segments:list[list[list]]) -> set[tuple[int, int]]:

    points = set()

    for segment in segments:
        for iCoord in range(1, len(segment)):
            pt1 = segment[iCoord - 1]
            pt2 = segment[iCoord]
            line = []
            if pt1[0] == pt2[0]:
                line = [(pt1[0], y) for y in range(min(pt1[1], pt2[1]), max(pt1[1], pt2[1]) + 1)]
            else:
                line = [(x, pt1[1]) for x in range(min(pt1[0], pt2[0]), max(pt1[0], pt2[0]) + 1)]
            for coord in line:
                points.add(coord)

    return points


def run_sand(input:list[str], add_floor):
    segments = [parseLine(line) for line in input]
    allTheCoords = reduce(lambda acc, sg: acc + sg, segments, [[500, 0]])
    
    xCoords = list(map(lambda p: p[0], allTheCoords))
    yCoords = list(map(lambda p: p[1], allTheCoords))

    minX = min(xCoords)
    maxX = max(xCoords)
    minY = min(yCoords)
    maxY = max(yCoords)

    points = expandLines(segments)
    startpoints = points.copy()
    sandUnits = 0

    if(add_floor):
        maxY +=2
    
    
    #print_things(startpoints, [], minX, minY, maxX, maxY)

    while True:
        pos = (500, 0)
        for x in range(0, 1000):


            if(pos[1] > maxY):
                #print_things(startpoints, points, minX, minY, maxX, maxY)
                return sandUnits
            
            if add_floor and (pos[1] == maxY - 1):
                points.add(pos)
                break
            
            if (pos[0], pos[1] + 1) in points:
                if (pos[0]-1, pos[1] + 1) in points:
                    if (pos[0]+1, pos[1] + 1) in points:
                        if(pos in points):
                            #print_things(startpoints, points, minX, minY, maxX, maxY)
                            return sandUnits
                        else:
                            points.add(pos)
                            break
                    else:
                        pos = (pos[0]+1, pos[1] + 1)
                else:
                    pos = (pos[0]-1, pos[1] + 1)
            else:
                pos = (pos[0], pos[1] + 1)


            if(x > 900):
                print_things(startpoints, points, minX, minY, maxX, maxY)
                raise "oops"

        sandUnits+=1

def result(input):
    return run_sand(input, False)


def print_things(startpoints, points, minx, miny, maxx, maxy):
    for y in range(miny, maxy+1):
        for x in range(minx, maxx+1):
            if((x, y) in startpoints):
                print("#", end="")
            elif((x, y) in points):
                print("o", end="")
            else:
                print(".", end="")
        print("")
    print("====")