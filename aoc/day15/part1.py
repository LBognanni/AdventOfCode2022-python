# Advent of Code - Day 15 - Part One
import re

def parse_input(lines:list[str]):
    expr = re.compile(r'[-]*\d+')
    for line in lines:
        things = expr.findall(line)
        yield [(int(things[0]), int(things[1])), (int(things[2]), int(things[3]))]
    

def get_dist(sensor, beacon) -> int:
    return abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1])

def get_area_line(beaconSensor:list[tuple[int, int]], y) -> list[tuple[int, int]]:
    sensor = beaconSensor[0]
    beacon = beaconSensor[1]
    d = get_dist(sensor, beacon)
    dist = d - abs(sensor[1] - y)
    
    for x in range(sensor[0] - dist, sensor[0] + dist + 1):
        if(x == beacon[0] and y == beacon[1]):
            continue
        yield x

def is_interesting(beacon: list[tuple[int, int]], line: int) -> bool:
    d = get_dist(beacon[0], beacon[1])
    return (beacon[0][1] -d) <= line <= (beacon[0][1] +d )

def result(input, line = 2000000):
    beacons = list(parse_input(input))

    interestingBeacons = list(filter(lambda b: is_interesting(b, line), beacons))

    pointsInLine = [x for b in interestingBeacons for x in get_area_line(b, line)]

    return len(set(pointsInLine))
