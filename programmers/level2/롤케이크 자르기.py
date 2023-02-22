from collections import Counter


def solution(topping):
    right_topping_kind_map = Counter(topping)
    left_topping_kind_map = {}
    fair_count = 0
    for i in range(len(topping)):
        if topping[i] not in left_topping_kind_map:
            left_topping_kind_map[topping[i]] = 0

        left_topping_kind_map[topping[i]] += 1
        right_topping_kind_map[topping[i]] -= 1

        if right_topping_kind_map[topping[i]] == 0:
            del right_topping_kind_map[topping[i]]

        if len(right_topping_kind_map) == len(left_topping_kind_map):
            fair_count += 1
    return fair_count
