from aoc.day21.part1 import Monkey, MonkeyType, Traverse

# Advent of Code - Day 21 - Part Two

def to_expr(monkeys:dict[str,Monkey], who):

    if not isinstance(who, str):
        return who

    if(who == "humn"):
        return "X"

    m = monkeys[who]
    if(m.Type == MonkeyType.Value):
        return m.Value

    return "({} {} {})".format(to_expr(monkeys, m.Left), m.Operation, to_expr(monkeys, m.Right))


def reverse(monkeys:dict[str, Monkey], curr:str, value:int):
    if(curr == "humn"):
        return value

    m = monkeys[curr]

    if(not isinstance(m.Left, str)):
        right = monkeys[m.Right]
        if m.Operation == "+":
            return reverse(monkeys, right.Name, value - m.Left)
        elif m.Operation == "-":
            return reverse(monkeys, right.Name, value - m.Left)
        elif m.Operation == "*":
            return reverse(monkeys, right.Name, int(value / m.Left))
        elif m.Operation == "/":
            return reverse(monkeys, right.Name, int(value / m.Left))
    else:
        left = monkeys[m.Left]
        if m.Operation == "+":
            return reverse(monkeys, left.Name, value - m.Right)
        elif m.Operation == "-":
            return reverse(monkeys, left.Name, value + m.Right)
        elif m.Operation == "*":
            return reverse(monkeys, left.Name, int(value / m.Right))
        elif m.Operation == "/":
            return reverse(monkeys, left.Name, value * m.Right)
        


def result(input):
    monkeysList = [Monkey(line) for line in input]
    monkeys = {m.Name:m for m in monkeysList}
    
    find = "humn"
    parents = []
    while(find != "root"):
        parent = [m for m in monkeysList if m.Type == MonkeyType.Operation and (m.Left == find or m.Right == find)][0]
        if(parent.Left == find):
            parent.Right = Traverse(monkeys, parent.Right)
        else:
            parent.Left  = Traverse(monkeys, parent.Left)
        parents.insert(0, parent.Name)
        find = parent.Name

    root = monkeys["root"]
    root.Operation = "="
    if(root.Left == parents[1]):
        val = Traverse(monkeys, root.Right)
        root.Right = val
        print(to_expr(monkeys, "root"))
        print ("result should be", 3220993874133)
        return reverse(monkeys, root.Left, val)
    else:
        val = Traverse(monkeys, root.Left)
        root.Left = val
        print(to_expr(monkeys, "root"))
        print ("result should be", 3220993874133)
        return reverse(monkeys, root.Right, val)
    

    return None
