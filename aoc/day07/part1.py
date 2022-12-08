# Advent of Code - Day 7 - Part One

def update_size(folders, current, size):
    folders[current]["size"] += size
    if folders[current]["parent"] != "":
        update_size(folders, folders[current]["parent"], size)


def result(input):
    folders = {
        "//": {
            "name": "//",
            "parent": "",
            "size": 0
        }
    }
    current = "/"
    parent = ""
    
    for line in input:
        if(line[0] == "$"):
            commands = line.split(" ")
            if commands[1] == "cd":
                if commands[2] == "..":
                    current = folders[current]["parent"]
                elif commands[2] == "/":
                    current = "/"
                    parent = ""
                else:
                    parent = current
                    current = current + "/" + commands[2]

                defaultFolder = {
                    "name": current,
                    "parent": parent,
                    "size": 0
                }

                folders[current] = folders.get(current, defaultFolder)
        else:
            content = line.split(" ")
            if content[0] != "dir":
                update_size(folders, current, int(content[0]))

    return sum(filter(lambda x: x<=100000, map(lambda x: x["size"], folders.values())))
