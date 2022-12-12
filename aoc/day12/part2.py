# Advent of Code - Day 12 - Part Two]
from aoc.day12 import part1


def result(input):

    heightmap = [[0 for c in l] for l in input]
    start = (0,0)
    end = (0,0)
    start_points = []

    for y in range(0, len(input)):
        for x in range(0, len(input[y])):
            if input[y][x] == "S":
                start = (y, x)
                heightmap[y][x] = 0
            elif input[y][x] == "E":
                end = (y, x)
                heightmap[y][x]= ord('z') - ord('a')
            else:
                heightmap[y][x] = ord(input[y][x]) - ord('a')

            if heightmap[y][x] == 0:
                start_points.append((y, x))

    min_result = 99999999999999999

    for pt in start_points:
        visited = [[False for c in l] for l in input]
        trip = part1.traverse(heightmap, pt, end, visited) 
        if(trip):
            result = len(trip)
            if(result < min_result):
                min_result = result

    return min_result
