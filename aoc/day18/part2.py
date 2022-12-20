# Advent of Code - Day 18 - Part Two

def find_cubes(input: list[str]):
    for cube in input:
        yield tuple(int(c) for c in cube.split(","))

def flood_fill(cubes:list[tuple[int, int, int]]):
    min_x = min([x for x,y,z in cubes]) - 1
    max_x = max([x for x,y,z in cubes]) + 1
    min_y = min([y for x,y,z in cubes]) - 1
    max_y = max([y for x,y,z in cubes]) + 1
    min_z = min([z for x,y,z in cubes]) - 1
    max_z = max([z for x,y,z in cubes]) + 1
    
    seen = set()

    investigating = [(min_x, min_y, min_z)]
    
    while(len(investigating) > 0):
        cube = investigating.pop()
        if cube not in cubes and cube not in seen:
            seen.add(cube)
            (x,y,z) = cube
            if x < max_x:
                investigating.append((x + 1, y, z))
            if y < max_y:
                investigating.append((x, y + 1, z))
            if z < max_z:
                investigating.append((x, y, z + 1))
            if x > min_x:
                investigating.append((x - 1, y, z))
            if y > min_y:
                investigating.append((x, y - 1, z))
            if z > min_z:
                investigating.append((x, y, z - 1))

    return (seen, max_x - min_x + 1, max_y - min_y + 1, max_z - min_z + 1)

def is_neighbour(cube1, cube2):
    (x1, y1, z1) = cube1
    (x2, y2, z2) = cube2
    if(abs(x1 - x2) == 1) and y1 == y2 and z1 == z2:
        return True
    if(abs(y1 - y2) == 1) and x1 == x2 and z1 == z2:
        return True
    if(abs(z1 - z2) == 1) and y1 == y2 and x1 == x2:
        return True
    return False

def has_neighbour(cube, others):
    return sum([1 for c in others if is_neighbour(c, cube)])

def result(input:list[str]):
    cubes = list(find_cubes(input))
    (outside, width, height, depth) = flood_fill(cubes)

    return sum([6 - has_neighbour(c, outside) for c in outside]) - ((height * width * 2) + (width * depth * 2) + (height * depth * 2) )
