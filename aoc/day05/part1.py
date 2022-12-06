# Advent of Code - Day 5 - Part One

def parse_body(line):
    arr = line.split(" ")
    return (int(arr[1]), arr[3], arr[5])

def parse(lines:list[str]):
    separator = lines.index("")
    header = lines[:separator-1]
    legend = lines[separator-1]
 
    body = lines[separator+1:]
    stacks = {}

    for i in range(len(legend)):
        if legend[i] == " ":
            continue
        for h in header:
            if(len(h)>= i) and (h[i] != " "):
                stack:list[str] = stacks.get(legend[i], [])
                stack.append(h[i])
                stacks[legend[i]] = stack
    
    movements = list(map(parse_body, body))

    return (stacks, movements)

def result(input):
    (stacks, movements) = parse(input)

    for (howMany, fromPos, toPos) in movements:
        els = stacks[fromPos][:howMany]
        stacks[toPos] = list(reversed(els)) + stacks[toPos]
        stacks[fromPos] = stacks[fromPos][howMany:]

    return "".join(map(lambda x:x[0], stacks.values()))