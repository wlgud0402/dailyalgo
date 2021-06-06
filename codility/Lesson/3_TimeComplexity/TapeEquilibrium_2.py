def solution(A):
    diff = 1e9
    right = sum(A)
    left = 0
    for i, v in enumerate(A):
        left += v
        right -= v

        if diff > abs(left - right):
            diff = abs(left - right)

    return diff


print(solution([1, 3]))  # 1
