from math import gcd


def solution(arr):
    new = 0
    for i in range(len(arr)-1):
        new = (arr[0] * arr[1]) // gcd(arr[0], arr[1])
        arr.pop(0)
        arr.pop(0)

        arr.insert(0, new)

    return new


print(solution([2, 6, 8, 14]))
# 168
