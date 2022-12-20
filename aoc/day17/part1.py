# Advent of Code - Day 17 - Part One


def result(input, n = 2022):

    if(len(input) == 1):
        input = input[0]

    rocks = [
        [(0,0), (1,0), (2, 0), (3, 0)],         # -
        [(0,1), (1,0), (1,1), (1,2), (2,1)],    # +
        [(0,0), (1,0), (2,0), (2,1), (2,2)],    # reverse L
        [(0,0), (0,1), (0,2), (0,3)],           # |
        [(0,0), (0,1), (1,0), (1,1)]            # []
    ]
    widths = [4,3,3,1,2]
    heights = [1,3,3,4,2]

    floor = [0 for n in range(0,7)]
    set_points = set([(n, 0) for n in range(0, 7)])

    rock_idx = 0
    direction_idx = 0
    for i in range(0, n):
        start = max(floor) + 4
        thisRock = [(pt[0] + 2, pt[1] + start)  for pt in rocks[rock_idx % len(rocks)]]
        rockHasStopped = False

        while not rockHasStopped:
            
            rockPos = []
            add = -1 if input[direction_idx % len(input)] == "<" else 1
            for pt in thisRock:
                x = pt[0] + add
                if x < 0 or x >=7 or (x, pt[1]) in set_points:
                    rockPos = thisRock
                    break
                rockPos.append((x, pt[1]))
            thisRock = rockPos
            direction_idx += 1
            
            rockPos = []
            for pt in thisRock:
                y = pt[1] - 1
                if (pt[0], y) in set_points:
                    rockPos = thisRock
                    rockHasStopped = True
                    break
                rockPos.append((pt[0], y))
            thisRock = rockPos

        for pt in thisRock:
            set_points.add(pt)

        for x in range(0, 7):
            floor[x] = max(floor[x], max([pt[1] for pt in thisRock if pt[0] == x] + [0]))


        rock_idx += 1

    return max(floor)
