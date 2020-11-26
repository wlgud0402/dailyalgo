from itertools import combinations


def deleteDigit(n):
    number = str(n)
    bundle = list(set(combinations(number, len(number)-1)))
    answer = 0
    for i in range(len(bundle)):
        new = int(''.join(bundle[i]))
        if answer < new:
            answer = new
    return answer


print(deleteDigit(1001))
