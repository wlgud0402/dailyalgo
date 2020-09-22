def solution(A, B):
    answer = 0
    A.sort()
    B.sort(reverse=True)
    for i in range(len(A)):
        A[i] = A[i] * B[i]

    return sum(A)


print(solution([1, 4, 2], [5, 4, 4]))
