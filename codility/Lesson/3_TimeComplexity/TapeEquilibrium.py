def solution(A):
    diffs = set()
    right = sum(A)
    left = 0
    for i, v in enumerate(A):
        left += v
        right -= v

        diff = abs(left - right)
        diffs.add(diff)

    return min(diffs)


print(solution([1, 3]))  # 1

# 13
# 0
# left = 3 + 1 = 4
# right 10 -1 = 9
