# -*- coding: utf-8 -*-
def boxBlur(image):
    if len(image[0]) > len(image):
        box_size = len(image[0])-2
    else:
        box_size = len(image)-2
    new_box = []
    for i in range(1, box_size+1):
        one_box = []
        for j in range(1, box_size+1):
            try:
                new_point = int((image[i-1][j-1] + image[i-1][j] + image[i-1][j + 1]
                                 + image[i][j-1]+image[i][j]+image[i][j+1]
                                 + image[i+1][j-1]+image[i+1][j]+image[i+1][j+1])/9)

                one_box.append(new_point)
            except:
                break

        if one_box != []:
            new_box.append(one_box)

    return new_box


# print(boxBlur([[7, 4, 0, 1],
#                [5, 6, 2, 2],
#                [6, 10, 7, 8],
#                [1, 4, 2, 0]]))

# [[5, 4],
# [4, 4]]
print(boxBlur([[36, 0, 18, 9],
               [27, 54, 9, 0],
               [81, 63, 72, 45]]))

# [[40,30]]

# 실패하는 케이스 => 세로로 긴 형태의 경우 모자이크 처리가 잘 되지 않음
print(boxBlur([[2, 2, 2],
               [4, 4, 4],
               [2, 2, 2],
               [4, 4, 4]]))
