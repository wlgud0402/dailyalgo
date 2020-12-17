import copy


def solution(land):
    answer_list = []
    for i in range(len(land[0])):
        max_value = land[0][i]
        answer = max_value
        max_idx = land[0].index(max_value)
        new_land = copy.deepcopy(land)

        for j in range(1, len(land)):
            new_land[j][max_idx] = 0
            max_value = max(new_land[j])
            answer += max_value
            max_idx = new_land[j].index(max_value)

        answer_list.append(answer)

    return max(answer_list)


print(solution([[1, 2, 3, 5], [5, 6, 7, 8],
                [4, 3, 2, 1]]	))  # 16
