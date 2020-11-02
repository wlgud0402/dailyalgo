# -*- coding: utf-8 -*- boxblur와 유사하다 ( 가로 세로에 따라 범위가 달라지고 이에따라 다르게 for문이 돌면서 i, j 를 특정)
def minesweeper(matrix):
    new_matrix = []
    for i in range(len(matrix)):
        add = []
        for j in range(len(matrix[0])):
            if matrix[i][j] == True:
                add.append(1)
            else:
                add.append(0)
        new_matrix.append(add)

    for i in range(len(new_matrix)):
        new_matrix[i].insert(0, 0)
        new_matrix[i].append(0)

    new_matrix.insert(0, [0]*len(new_matrix[0]))
    new_matrix.append([0]*len(new_matrix[0]))

    whole_box = []
    for i in range(1, len(new_matrix)-1):
        one_line = []
        one_point = 0
        for j in range(1, len(new_matrix[0])-1):
            one_point = int(sum(new_matrix[i-1][j-1:j+2]))\
                + new_matrix[i][j-1] + new_matrix[i][j+1] + \
                int(sum(new_matrix[i+1][j-1:j+2]))
            one_line.append(one_point)
        whole_box.append(one_line)
    return whole_box


print(minesweeper([[True, False, False, True],
                   [False, False, True, False],
                   [True, True, False, True]]))
# 주변의 마인 갯수를 보여주는 새로운 행렬을 만들기 => 마인:True, 빈곳:False
