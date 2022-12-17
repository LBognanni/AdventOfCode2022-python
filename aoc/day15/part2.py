# Advent of Code - Day 15 - Part Two
from aoc.day15 import part1
import math
from typing import Iterable

def intersects(square1:tuple[int, int, int, int], square2: tuple[int, int, int, int]) -> bool:
    (s1x1,s1y1,s1x2,s1y2) = square1
    (s2x1,s2y1,s2x2,s2y2) = square2
    return not (s1x2<s2x1 or s2x2<s1x1 or s1y2<s2y1 or s2y2<s1y1)

# A sensor is "interesting" if it intersects the area we care about
def is_sensor_interesting(beacon, areaSize) -> bool:
    d = part1.get_dist(beacon[0], beacon[1])
    return intersects((0,0, areaSize, areaSize), (beacon[0][0] - d, beacon[0][1] - d, beacon[0][0] + d, beacon[0][1] + d))


def get_possible_x_range(sensors:list[tuple[tuple[int,int], int, int]], y: int, areaSize: int) -> Iterable[int]:
    # get min-max x ranges for all sensors
    ranges = [get_area_line(s, y) for s in sensors]
    
    # merge &  invert ranges
    x = 0
    while x <= areaSize:
        possibles = filter(lambda r: any(r) and (x >= r[0] and x <= r[1]), ranges)
        x1 = max(map(lambda r: r[1], possibles), default=-1)
        if x < x1:
            x = x1
        else:
            yield x
        x += 1

def get_area_line(sensor: tuple[tuple[int, int], int], y: int) -> list[int, int]:
    (px,py) = sensor[0]
    d = sensor[1]
    if py - d > y:
        return[]
    if py + d < y:
        return[]

    dd = d - abs(py - y)
    return [px - dd, px + dd]


def result(input:list[str], areaSize: int = 4_000_000):
    sensorsAndBeacons = part1.parse_input(input)
    interestingSensors = list(map(lambda b: (b[0], part1.get_dist(b[0], b[1]), math.ceil(part1.get_dist(b[0], b[1]) / 2)), filter(lambda b: is_sensor_interesting(b, areaSize), sensorsAndBeacons)))

    for y in range(0, areaSize):
        r = get_possible_x_range(interestingSensors, y, areaSize)
        x = next(r, None)
        if x != None:
            return (x * 4000000) + y

    return None
