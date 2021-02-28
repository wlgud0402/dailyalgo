comb = []


def solution(balls, weight):
    for i in range(len(balls)):
        for j in range(i, len(balls)):
            if balls[i] != balls[j]:
                comb.append([i+1, j+1])
    print(comb)


print(solution([1, 3, 2, 3, 2], 3))
