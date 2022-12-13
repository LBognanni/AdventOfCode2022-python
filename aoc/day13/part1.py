# Advent of Code - Day 13 - Part One
import json
import collections


def parse_line(line:str) -> list:
    return json.loads(line)

def parse_pairs(lines:list[str]) -> list[tuple[list, list]]:
    found = []
    items = []
    for line in lines:
        if(line == ""):
            items.append((found[0], found[1]))
            found = []
        else:
            found.append(parse_line(line))
    
    if(found):
        items.append((found[0], found[1]))
    
    return items

def compare_things(left, right) -> int:
    is_array_left = isinstance(left, collections.Sequence)
    is_array_right = isinstance(right, collections.Sequence)

    if is_array_left:
        if is_array_right:
            for i in range(0, min([len(left), len(right)])):
                result = compare_things(left[i], right[i])
                if result != 0:
                    return result

            if len(left) < len(right):
                return -1
            elif len(left) > len(right):
                return 1

            return 0 # they're the same
        else:
            return compare_things(left, [right])
    else:
        if is_array_right:
            return compare_things([left], right)
        else:
            if left < right:
                return -1
            elif left == right:
                return 0
            else: 
                return 1


def result(input):
    items = parse_pairs(input)
    result = 0

    for i in range(0, len(items)):
        if compare_things(items[i][0], items[i][1]) == -1:
            result += (i+1)
    
    return result
