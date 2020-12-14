def rotateImage(a):
    box = []
    for i in range(len(a)):
        one_line = []
        for j in range(len(a)):
            one_point = a[j][i]
            one_line.insert(0, one_point)

        box.append(one_line)

    return box


print(rotateImage([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]]))

# rotate '90' degree
# [[7, 4, 1],
#  [8, 5, 2],
#  [9, 6, 3]]
