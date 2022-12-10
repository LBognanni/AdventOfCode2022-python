# Advent of Code - Day 9 - Part One

strategy = {
    "D": lambda x,y: (x, y+1),
    "U": lambda x,y: (x, y-1),
    "L": lambda x,y: (x-1, y),
    "R": lambda x,y: (x+1, y)
}

def move_tail(tail_pos, head_pos):
    (hx,hy) = head_pos
    (tx, ty) = tail_pos
    dx = hx - tx
    dy = hy - ty
    
    if -1 <= dx <= 1 and -1 <= dy <= 1:
        return (tx, ty)
    
    if dx == -2:
        return (tx - 1, ty + dy)
    if dx == 2:
        return (tx + 1, ty + dy)
    if dy == -2:
        return (tx + dx, ty - 1)
    if dy == 2:
        return (tx + dx, ty + 1)
        
    return (tx, ty)

def result(input:list[str]):

    tail_positions = set()
    head_position = (0,0)
    tail_position = (0,0)

    for s in input:
        parts = s.split(" ")
        where = parts[0]
        n = int(parts[1])
        for i in range(0, n):
            (x,y) = head_position
            head_position = strategy[where](x,y)
            tail_position = move_tail(tail_position, head_position)
            tail_positions.add(tail_position)

    return len(tail_positions)
