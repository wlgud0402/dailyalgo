from collections import Counter


def solution(want, number, discount):
    possible_day_count = 0

    want_map = {}
    for w, n in zip(want, number):
        want_map[w] = n

    for i in range(len(discount)-9):
        discount_map = Counter(discount[i:i+10])
        if discount_map == want_map:
            possible_day_count += 1

    return possible_day_count


print(solution(["a", "b", "c"],
               [1, 1, 1],
               ["a", "a", "c", "a", "a", "a", "a", "a", "b", "c"]))
