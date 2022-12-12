# Advent of Code - Day 12 - Part One


def can_travel(cur, next):
    if next == (cur+1) or next <= cur:
        return True
    return False

def add_neighbours(pt:tuple[int, int], heightmap:list[list[int]], moves:list, candidates:list, end:tuple[int, int], visited):
    (y, x) = pt
    curr = heightmap[y][x]

    positions = []

    if y > 0:
        if can_travel(curr, heightmap[y-1][x]):
            positions.append((y-1, x))
    if x > 0:
        if can_travel(curr, heightmap[y][x-1]):
            positions.append((y, x-1))
    if y < (len(heightmap)-1):
        if can_travel(curr, heightmap[y+1][x]):
            positions.append((y+1, x))
    if x < (len(heightmap[y])-1):
        if can_travel(curr, heightmap[y][x+1]):
            positions.append((y, x+1))
    
    for pos in positions:
        if not pos in moves:
            (y,x) = pos
            if visited[y][x]:
                continue
            visited[y][x] = True
            next_moves = moves.copy()
            next_moves.add(pt)
            candidates.append((pos, next_moves))

def dist(pt, end):
    return ((pt[0] - end[0])**2 + (pt[1] - end[1])**2)

def traverse(heightmap:list[list[tuple[int, int]]], start:tuple[int,int], end:tuple[int,int], visited):
    candidates = []

    add_neighbours(start, heightmap, set([start]), candidates, end, visited)

    while len(candidates):
        next_candidates = []
        
        for candidate in candidates:
            (pt, moves) = candidate
            if pt == end:
                return moves
            else:
                add_neighbours(pt, heightmap, moves, next_candidates, end, visited)

        candidates = next_candidates

    return None


def result(input):

    heightmap = [[0 for c in l] for l in input]
    visited = [[False for c in l] for l in input]
    start = (0,0)
    end = (0,0)

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

    result = traverse(heightmap, start, end, visited)
    

    for y in range(0, len(input)):
        for x in range(0, len(input[y])):
            if ((y,x)) in result:
                print("X", end="")
            else:
                print(".", end="")
        print("")


    return len(result)
