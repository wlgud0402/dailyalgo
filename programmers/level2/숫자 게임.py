def solution(A, B):
    A.sort()
    B.sort()

    winner_count = 0
    for i in range(len(A)):
        is_win = False
        for j in range(len(B)):
            if A[i] < B[j]:
                winner_count += 1
                B.pop(j)
                is_win = True
                break
        if not is_win:
            B.pop(0)
    return winner_count


print(solution([5, 1, 3, 7], [2, 2, 6, 8]))
