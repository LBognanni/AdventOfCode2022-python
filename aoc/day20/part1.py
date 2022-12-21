# Advent of Code - Day 20 - Part One


def move_numbers(numbers:list[int]):
    indices = list(range(len(numbers)))
    for ix, moveBy in enumerate(numbers):
        pos = (indices.index(ix) + moveBy) % (len(numbers) - 1)
        indices.remove(ix)
        if(pos == 0):
            indices.append(ix)
        else:
            indices.insert(pos, ix)

    return [numbers[i] for i in indices]


def result(input:list[str]):
    numbers = move_numbers(list(map(int, input)))
    idx = numbers.index(0)

    return  numbers[(idx + 1000) % len(numbers)] + \
            numbers[(idx + 2000) % len(numbers)] + \
            numbers[(idx + 3000) % len(numbers)]
