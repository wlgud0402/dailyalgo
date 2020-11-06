# -*- coding: utf-8 -*-
import numpy as np  # 패키지 불러오기


def solution(arr1, arr2):
    arr1 = np.mat(arr1)
    arr2 = np.mat(arr2)

    new_arr = arr1 * arr2

    answer = []
    for i in range(len(arr1)):
        one_line = []
        for j in range(len(arr2)):
            one_line.append(int(np.array(new_arr)[i][j]))
        answer.append(one_line)
    return answer


print(solution([[1, 4], [3, 2], [4, 1]]	, [[3, 3], [3, 3]]))
