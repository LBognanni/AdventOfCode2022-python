# Advent of Code - Day 8 - Part One

def scan_x(grid, find, compare):
    visibles = []

    for y in range(1, len(grid)-1):
        max_found = 0
        for x in range(1, len(grid[0])-1):

            (find_x, find_y) = find(x,y)
            (compare_x, compare_y) = compare(x,y)
            find_val = int(grid[find_y][find_x])
            compare_val = max([int(grid[compare_y][compare_x]), max_found])

            if find_val > compare_val:
                visibles.append((find_x,find_y, find_val))
                max_found = find_val
            elif max_found < compare_val:
                max_found = compare_val
            
    return visibles

def scan_y(grid, find, compare):
    visibles = []

    for x in range(1, len(grid[0])-1):
        max_found = 0
        for y in range(1, len(grid)-1):

            (find_x, find_y) = find(x,y)
            (compare_x, compare_y) = compare(x,y)
            find_val = int(grid[find_y][find_x])
            compare_val = max([int(grid[compare_y][compare_x]), max_found])
            

            if find_val > compare_val:
                visibles.append((find_x,find_y, find_val))
                max_found = find_val
            elif max_found < compare_val:
                max_found = compare_val
    
    return visibles


def result(grid:list[str]):
    w = len(grid[0])
    h = len(grid)
    visible_xInc = scan_x(grid, lambda x,y: (x,y), lambda x,y: (x-1,y))
    visible_xDec = scan_x(grid, lambda x,y: (w - x - 1, y), lambda x,y: (w - x, y))
    visible_yInc = scan_y(grid, lambda x,y: (x,y), lambda x,y: (x,y-1))
    visible_yDec = scan_y(grid, lambda x,y: (x, h - y - 1), lambda x,y: (x, h - y))

    all = set(visible_xInc + visible_xDec + visible_yInc + visible_yDec)
    
    return len(all) + (w*2) + (h*2) - 4
