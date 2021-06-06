def solution(A):
    if len(A) == 1:
        return 1
    A.sort()
    for i in range(1, len(A)):
        if A[i-1]+1 != A[i]:
            return A[i] - 1


print(solution([2]))
