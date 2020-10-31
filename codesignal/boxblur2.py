# -*- coding: utf-8 -*-
def boxBlur(image):
    box_size = len(image[0])-2
    new_box = []
    for i in range(1, box_size+1):
        one_box = []
        for j in range(1, box_size+1):
            try:
                new_point = int(sum(image[i-1][j-1:j+2]
                                    + image[i][j-1:j+2]
                                    + image[i+1][j-1:j+2])/9)
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
