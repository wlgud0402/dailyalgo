def solution(A, K):
    if A == []:
        return []
    for i in range(K):
        last = A.pop()
        A.insert(0, last)
    return A



print(solution([],3))

# [4,1,2,3] [3,4,1,2] [2,3,4,1] [1,2,3,4]