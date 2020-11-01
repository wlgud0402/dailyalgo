# -*- coding: utf-8 -*- boxblur와 유사하다 ( 가로 세로에 따라 범위가 달라지고 이에따라 다르게 for문이 돌면서 i, j 를 특정)
def minesweeper(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == True:
                matrix[i][j] = 1
            else:
                matrix[i][j] = 0

    print(matrix)

    new_map = []
    for i in range(len(matrix)):
        one_line = []
        one_point = 0
        for j in range(1, len(matrix[0])):
            one_point = matrix[i-1][j-1:j+2]
            print(i, j)
            # print("one_point: ", one_point)
            #     one_point = sum(matrix[i-1][j-1:j+2] +
            #                     matrix[i][j-1:j+2] + matrix[i+1][j-1:j+2])
            #     if matrix[i][j] == 1:
            #         one_point -= 1
            #     one_line.append(one_point)
            # new_map.append(one_line)
    print(new_map)


print(minesweeper([[True, False, False],
                   [False, True, False],
                   [False, False, False]]))
# 주변의 마인 갯수를 보여주는 새로운 행렬을 만들기 => 마인:True, 빈곳:False
