# Advent of Code - Day 25 - Part One

snafuConvert = {
    "2": 2,
    "1": 1,
    "0": 0,
    "-": -1,
    "=": -2
}


def snafuToDec(s:str) -> int:
    pos = len(s) - 1
    res = 0
    for c in s:
        res += snafuConvert[c] * pow(5, pos)
        pos -= 1
    return res

def decToSnafu(n: int) -> str:

    output = ""
    if(n > 0):
        div, mod = divmod(n+2, 5)
        return decToSnafu(div) + '=-012'[mod]

    return output


def result(input:list[str]):
    return decToSnafu(sum([snafuToDec(s) for s in input]))
