from math import gcd


def solution(n, m):
    if n > m:
        large = n
        small = m
    else:
        large = m
        small = n

    max_div = gcd(large, small)
    min_mult = (large * small) // max_div
    return [max_div, min_mult]


print(solution(3, 12))
#[3, 12]
