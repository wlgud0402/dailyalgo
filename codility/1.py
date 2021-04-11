def solution(A, K):
    for i in range(K):
        A = [A[-1]] + A[:-1]
    return A


print(solution([3, 8, 9, 7, 6], 3))  # [9, 7, 6, 3, 8]
