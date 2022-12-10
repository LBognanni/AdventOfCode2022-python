from aoc.day09 import part1

# Advent of Code - Day 9 - Part Two

def result(input):

    rope_length = 10

    nodes = [(0,0) for n in range(0,rope_length)]
    tail_positions = set()

    for s in input:
        parts = s.split(" ")
        where = parts[0]
        n = int(parts[1])
        for i in range(0, n):
            (x,y) = nodes[0]
            nodes[0] = part1.strategy[where](x,y)
            for iN in range(1, rope_length):
                nodes[iN] = part1.move_tail(nodes[iN], nodes[iN-1])
            tail_positions.add(nodes[rope_length-1])
        #print_journey(nodes)
    
    #print_journey(tail_positions)
    return len(tail_positions)




def print_journey(positions):
    xs = list(map(lambda p: p[0], positions))
    ys = list(map(lambda p: p[1], positions))
    minX = min(xs) - 1
    minY = min(ys) - 1
    maxX = max(xs) + 1
    maxY = max(ys) + 1
    w = maxX - minX
    h = maxY - minY
    grid = [["." for n in range(0, w)] for n in range(0, h)]

    i = 0
    for pos in positions:
        (x,y) = pos
        grid[y-minY][x - minX] = str(i) if i < 10 else "#"
        i+=1

    print("")

    for line in grid:
        print("".join(line))