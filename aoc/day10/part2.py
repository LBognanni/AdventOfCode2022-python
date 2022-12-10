# Advent of Code - Day 10 - Part Two

def result(input):

    screen_line = []
    screen = []
    cycle = 0
    x = 1

    def run_cycle(a):
        nonlocal cycle, screen, x, screen_line

        d = cycle % 40

        if (d == 0):
            screen.append("".join(screen_line))
            screen_line = ["." for n in range(0, 40)]
            
        if (x-1) <= d <= (x+1):
            screen_line[d] = "#"

        x+=a
        cycle+=1

    for line in input:
        run_cycle(0)
        if line != "noop":
            add = int(line.split(" ")[1])
            run_cycle(add)
    run_cycle(0)

    return "\n".join(screen)
