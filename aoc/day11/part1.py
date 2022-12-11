import math
# Advent of Code - Day 11 - Part One

class Operation:
    def __init__(self, str:str):
        parts = list(filter(lambda x: x!="", str.split("=")[1].split(" ")))
        self.left = parts[0]
        self.operator = parts[1]
        self.right = parts[2]

    def parseThing(self, val, str):
        if(str == "old"):
            return val
        return int(str)

    def run(self, val):
        if(self.operator == "+"):
            return self.parseThing(val, self.left) + self.parseThing(val, self.right)
        if(self.operator == "*"):
            return self.parseThing(val, self.left) * self.parseThing(val, self.right)
        return None
        

class Monkey:

    def __init__(self, items, operation, divide_by, monkey_true, monkey_false) -> None:
        self.items = items
        self.operation = operation
        self.divide_by = divide_by
        self.monkey_true = monkey_true
        self.monkey_false = monkey_false
        self.inbox = []
        self.times_inspected = 0

    def run(self, monkeys:list):
        for orig in self.items:
            item = math.floor(self.operation.run(orig) / 3)
            throw_to =  self.monkey_true if(item % self.divide_by == 0) else self.monkey_false
            monkeys[throw_to].items.append(item)
            self.times_inspected+=1
        self.items = []

def parse_input(lines:list[str]) -> list[Monkey]:

    if(lines[len(lines)-1])!="":
        lines.append("")
        
    monkeys = []
    items = []
    operation = None
    divide_by = 1
    monkey_true = 0
    monkey_false = 0

    for line in lines:
        if line == "":
            monkeys.append(Monkey(items, operation, divide_by, monkey_true, monkey_false))
        else:
            parts = list(filter(lambda x: x!="", line.split(" ")))
            if parts[0] == "Starting":
                items = list(map(int, line.split(":")[1].split(", ")))
            elif parts[0] == "Operation:":
                operation = Operation(line)
            elif parts[0] == "Test:":
                divide_by = int(parts[len(parts)-1])
            elif parts[1] == "true:":
                monkey_true = int(parts[len(parts)-1])
            elif parts[1] == "false:":
                monkey_false = int(parts[len(parts)-1])
    return monkeys



def result(input):

    monkeys = parse_input(input)
    rounds = 20

    for _ in range(0, rounds):
        for monkey in monkeys:
            monkey.run(monkeys)
        pass

    values = sorted(map(lambda m: m.times_inspected, monkeys), reverse=True)

    return values[0] * values[1]
