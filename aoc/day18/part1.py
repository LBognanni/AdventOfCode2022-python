# Advent of Code - Day 18 - Part One
import collections

def find_faces(cubes:list[str]):

    for cube in cubes:
        p = [int(c) for c in cube.split(",")]
        yield ("L", p[0], p[1], p[2])
        yield ("D", p[0], p[1], p[2])
        yield ("F", p[0], p[1], p[2])

        yield ("L", p[0] + 1, p[1], p[2])
        yield ("D", p[0], p[1] + 1, p[2])
        yield ("F", p[0], p[1], p[2] + 1)

def result(input:list[str]):
    faces = list(find_faces(input))
    facesDict = collections.defaultdict(lambda: 0)

    for face in faces:
        facesDict[face] += 1


    return len([v for v in facesDict.values() if v == 1])
