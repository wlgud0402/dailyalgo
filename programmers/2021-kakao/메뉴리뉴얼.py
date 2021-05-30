from itertools import combinations


def solution(orders, course):
    answers = set()
    for order in orders:
        for i in range(2, len(orders)):
            possibles = list((combinations(order, i)))
            for j in range(len(orders)):
                if


print(solution(["XYZ", "XWY", "WXA"], [2, 3, 4]))
# ["WX", "XY"]
