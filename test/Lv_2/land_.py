def solution(land):
    answer = []
    for i in range(len(land)):
        try:
            max_num = max(land[i])
            answer.append(max_num)

            max_idx = land[i].index(max_num)
            land[i+1][max_idx] = 0
        except:
            return sum(answer)


print(solution([[1, 2, 3], [2, 2, 2], [2, 3, 1]]))
