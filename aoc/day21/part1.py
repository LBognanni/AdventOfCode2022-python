# Advent of Code - Day 21 - Part One
from enum import Enum

# class syntax

class MonkeyType(Enum):
    Value = 1
    Operation = 2

class Monkey:
    def __init__(self, text:str):
        parts = text.split(": ")
        self.Name = parts[0]
        if(parts[1].isnumeric()):
            self.Value = int(parts[1])
            self.Type = MonkeyType.Value
        else:
            operation = parts[1].split(" ")
            self.Left = operation[0]
            self.Right = operation[2]
            self.Operation = operation[1]
            self.Type = MonkeyType.Operation

def Traverse(monkeys:dict[str, Monkey], who:str):
    if(not isinstance(who, str)):
        return who
        
    monkey:Monkey = monkeys[who]
    if(monkey.Type == MonkeyType.Value):
        return monkey.Value
    
    left = Traverse(monkeys, monkey.Left)
    right = Traverse(monkeys, monkey.Right)
    if monkey.Operation == "+":
        return left + right
    elif monkey.Operation == "-":
        return left - right
    elif monkey.Operation == "*":
        return left * right
    elif monkey.Operation == "/":
        return int(left / right)
    
    raise ValueError("Unknown operation")


def result(input:list[str]):
    monkeys = {m.Name:m for m in [Monkey(line) for line in input]}
    return Traverse(monkeys, "root")
