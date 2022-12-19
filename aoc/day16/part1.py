# Advent of Code - Day 16 - Part One
from typing import Iterable
import re
from functools import cache

class Path:
    def __init__(self, to:str, cost:int, via:list[str]) -> None:
        self.To = to
        self.Cost = cost
        self.Via = via

class Valve:
    def __init__(self, name:str, flow_rate:int, leads_to:list[str]) -> None:
        self.Name = name
        self.LeadsTo = leads_to
        self.FlowRate = flow_rate
        self.Paths = { p:Path(p, 1, []) for p in leads_to }


def parse_valves(input:list[str]) -> Iterable[Valve]:
    expr = re.compile(r'Valve (\w\w) has flow rate=([0-9]+); tunnel[s]* lead[s]* to valve[s]* ([A-Z\s,]+)')
    for line in input:
        matches = expr.match(line)
        yield Valve(matches.group(1), int(matches.group(2)), matches.group(3).split(", "))

def calculate_distances(valves:dict[str, Valve]):
    has_more = True
    dist = 1
    while has_more:
        has_more = False
        for key in valves:
            for sub in valves[key].LeadsTo:
                for path in valves[sub].Paths:
                    if (path not in valves[key].Paths) and (valves[sub].Paths[path].Cost == dist):
                        valves[key].Paths[path] = Path(path, dist + 1, valves[sub].Paths[path].Via + [sub])
            if len(valves[key].Paths) < len(valves):
                has_more = True
                
        dist += 1

    
def result(input):
    valves_list:list[Valve] = list(parse_valves(input))
    valves = { item.Name: item for item in valves_list}
    
    calculate_distances(valves)



    @cache
    def traverse(current_valve:str, open_valvesStr: str, minute: int, score: int) -> int:
        open_valves = list(filter(None, open_valvesStr.split(",")))
        not_open_valves = [k for k in valves if k not in open_valves and valves[k].FlowRate > 0]

        for idx in open_valves:
            score += valves[idx].FlowRate

        if minute >= 30:
            return score

        max_score = 0

        for valve in not_open_valves:
            # Option 1: I'm opening this valve
            if valve == current_valve:            
                thisscore = traverse(valve, open_valvesStr + "," + current_valve, minute + 1, score)
                if thisscore > max_score:
                    max_score = thisscore
                
            # Option 2: I'm skipping this valve
            thisscore = traverse(valve, open_valvesStr, minute + valves[current_valve].Paths[valve].Cost, score)
            if thisscore > max_score:
                max_score = thisscore

        return max_score


    released_pressure = traverse("AA", "", 1, 0)
    return released_pressure

    open_valves = []
    current_valve = "AA"
    released_pressure = 0
    
    i = 1
    while i <= 30:
        if(len(not_open_valves) > 0):
            next = not_open_valves[0][0]
            if next == current_valve:
                open_valves.append(current_valve)
            else:
                i += valves[current_valve].Paths[next].Cost
                current_valve = next

        for idx in open_valves:
            released_pressure += valves[idx].FlowRate
        i += 1

    return released_pressure

    
    

    #priority_list = sorted(valves_list, key=lambda v: v.FlowRate, reverse=True)
#
    #open_valves = []
    #current_valve = "AA"
    #released_pressure = 0
#
    #for i in range(0,30):
    #    possible_next_valves = list(sorted(filter(lambda v: v not in open_valves, valves[current_valve].LeadsTo), key=lambda v: valves[v].FlowRate, reverse=True))
    #    next_valve = possible_next_valves[0] if len(possible_next_valves) > 0 else "AA"
    #    
    #    if (not  current_valve in open_valves) and valves[current_valve].FlowRate > 0:
    #        current_potential = valves[current_valve].FlowRate * (30-i)
    #        next_potential = valves[next_valve].FlowRate * (30 - i -1)
    #        
    #        if(current_potential > next_potential):
    #            open_valves.append(current_valve)
    #        else:
    #            current_valve = next_valve
    #    else:
    #        current_valve = next_valve
#
    #    for idx in open_valves:
    #        released_pressure += valves[idx].FlowRate
    #
    #return released_pressure
