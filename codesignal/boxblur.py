def boxBlur(image):
    box_size = len(image[0])-2
    new_box = [[0]*box_size for i in range(box_size)]


print(boxBlur([[7, 4, 0, 1],
               [5, 6, 2, 2],
               [6, 10, 7, 8],
               [1, 4, 2, 0]]))

# [[5, 4],
# [4, 4]]
