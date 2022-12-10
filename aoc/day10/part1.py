# Advent of Code - Day 10 - Part One


def result(input:list[str]):

    s_str = 0
    cycle = 1
    x = 1

    def run_cycle(a):
        nonlocal cycle, s_str, x 
        cycle+=1
        x+=a
        if (cycle - 20) % 40 == 0:
            s_str += cycle * x

    for line in input:
        run_cycle(0)
        if line != "noop":
            add = int(line.split(" ")[1])
            run_cycle(add)

    return s_str
