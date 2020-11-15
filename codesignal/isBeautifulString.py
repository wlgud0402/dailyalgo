import collections


def isBeautifulString(inputString):
    inputString = ''.join(sorted(inputString))
    count = collections.Counter(inputString).items()
    count = sorted(count)

    max_count = count[0][1]
    ordinary = 2
    for i in range(1, len(count)):
        if ord(count[i][0]) - 96 != ordinary:
            return False
        ordinary += 1

        if max_count < count[i][1]:
            return False
    return True


print(isBeautifulString("abcdefghijklmnopqrstuvwxyz"))  # true
