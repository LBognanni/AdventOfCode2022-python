# Advent of Code - Day 8 - Part Two

def treesVisible(arr, cur):
    num_visible = 0

    if(arr == None):
        return 0

    for tree in arr:
        num_visible+=1
        if tree >= cur:
            break
    
    return num_visible

def brute_force(grid):
    max_score = 0

    w = len(grid[0])
    h = len(grid)

    for y in range(1, h - 1):
        for x in range(1, w - 1):
            to_the_left = grid[y][0:x][::-1]
            to_the_right = grid[y][x+1:w]
            to_the_top = list(map(lambda g: g[x], grid[0:y]))[::-1]
            to_the_bottom = list(map(lambda g: g[x], grid[y+1:h]))
            cur = grid[y][x]
            
            score = treesVisible(to_the_bottom, cur) * treesVisible(to_the_left, cur) * treesVisible(to_the_right, cur) * treesVisible(to_the_top, cur)

            if(score > max_score):
                max_score = score
    
    return max_score

def result(input):
    return brute_force(list(map(lambda line: [int(c) for c in line], input)))
