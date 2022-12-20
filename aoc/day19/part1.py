import re

# Advent of Code - Day 19 - Part One

class Blueprint:
    def __init__(self, text:str) -> None:
        parts = text.split(": ")
        self.Id = int(parts[0].split(" ")[1])
        costs = parts[1].split(". ")
        expr = re.compile(r'Each (\w+) robot costs ([0-9]+) (\w+)(?: and ([0-9]+) (\w+))?')
        self.Costs = {}

        for cost in costs:
            matches = expr.match(cost)
            matches = matches.groups()
            arr = []
            for i in range(1, len(matches), 2):
                if matches[i] == None:
                    break
                arr.append((matches[i+1], int(matches[i])))
            
            self.Costs[matches[0]] = arr

    def find_cost(self, of, material):
        for c in self.Costs[of]:
            if c[0] == material:
                return c[1]
        return None


class Simulation:
    def __init__(self, blueprint: Blueprint) -> None:
        self.Blueprint = blueprint
        self.resourceTypes = ["geode", "obsidian", "clay", "ore"]
        self.Resources = {r:0 for r in self.resourceTypes}
        self.Robots = {r:0 for r in self.resourceTypes}
        self.Robots["ore"] = 1
        self.cache = {}
        self.max_solution = 0

    def can_afford(self, resourceType, robots, minute):
        if resourceType == "obsidian":
            return robots["clay"] > 0
        if resourceType == "geode":
            return robots["obsidian"] > 0
        return True

    def run_for_wanted(self, wanted:str, resources:dict[str,int], robots:dict[str,int], minute:int):

        key = "{}_{}_{}_{}".format(wanted, ",".join(map(str,resources.values())), ",".join(map(str,robots.values())), minute)
        if key in self.cache.keys():
            return self.cache[key]
        
        found = False
        while not found and minute < self.max_minutes:
            
            newRobots = {r:0 for r in self.resourceTypes}
            found = True
            for (which, howmuch) in self.Blueprint.Costs[wanted]:
                if resources[which] < howmuch:
                    found = False
                    break

            if found:
                newRobots[wanted] += 1
                for (which, howmuch) in self.Blueprint.Costs[wanted]:
                    resources[which] -= howmuch
            
            for resource in self.resourceTypes:
                resources[resource] += robots[resource]
                robots[resource] += newRobots[resource]
            pass
            minute += 1

        if minute == (self.max_minutes):
            self.cache[key] = resources["geode"]
            self.max_solution = max(self.max_solution, resources["geode"])
            return resources["geode"]
        else:
            triangle_nums = [0, 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120, 136, 153, 171, 190, 210, 231, 253, 276, 300, 325, 351, 378, 406, 435, 465, 496, 528, 561, 595, 630]
            minutes_remaining = (self.max_minutes - minute)
            max_possible = resources["geode"] + robots["geode"] * minutes_remaining + triangle_nums[minutes_remaining]
            value = resources["geode"]
            if(max_possible > self.max_solution):
                possible_next = [wanted for wanted in  self.resourceTypes if self.can_afford(wanted, robots, minute)]
                if(len(possible_next) > 0):
                    value = max([self.run_for_wanted(wanted, resources.copy(), robots.copy(), minute) for wanted in possible_next])
                    
            self.cache[key] = value
            return value
        

    def run(self, minutes):
        self.max_minutes = minutes
        return max([
            self.run_for_wanted("ore", self.Resources.copy(), self.Robots.copy(), 0),
            self.run_for_wanted("clay", self.Resources.copy(), self.Robots.copy(), 0)
        ])
            


def result(input):
    simulations = [Simulation(Blueprint(x)) for x in input]
    return sum([s.run(24) * s.Blueprint.Id for s in simulations])
