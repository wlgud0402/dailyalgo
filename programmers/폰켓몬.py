from itertools import combinations


def solution1(nums):
    comb = list(combinations(nums, len(nums)//2))
    all_len = []
    for c in comb:
        s = set(c)
        all_len.append(len(s))

    all_len.sort()
    return all_len[-1]


def solution(nums):
    pick_count = len(nums)//2

    removed_double = list(set(nums))
    print(removed_double)

    if len(removed_double) >= pick_count:
        return pick_count

    if len(removed_double) < pick_count:
        return len(removed_double)

    # if len(removed_double) > pick_count:
    #     return pick_count


print(solution([3, 1, 2, 3]))  # 2
