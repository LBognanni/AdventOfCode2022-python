# Advent of Code - Day 20 - Part One


def move_numbers(numbers:list[int], times: int):
    indices = list(range(len(numbers)))

    for _ in range(times):
        for ix, moveBy in enumerate(numbers):
            if moveBy == 0:
                continue
            pos = (indices.index(ix) + moveBy) % (len(numbers) - 1)
            indices.remove(ix)
            if(pos == 0):
                indices.append(ix)
            else:
                indices.insert(pos, ix)
        #print(", ".join([str(numbers[i]) for i in indices]))

    return [numbers[i] for i in indices]


def result(input:list[str]):
    numbers = move_numbers(list(map(int, input)), 1)
    idx = numbers.index(0)

    return  numbers[(idx + 1000) % len(numbers)] + \
            numbers[(idx + 2000) % len(numbers)] + \
            numbers[(idx + 3000) % len(numbers)]
