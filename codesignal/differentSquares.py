# find 2x2
# When use Set() => you need to use form of tuple to add

def differentSquares(matrix):
    answer = []
    for i in range(len(matrix)-1):
        for j in range(len(matrix[0])-1):
            box = [[matrix[i][j], matrix[i][j+1]],
                   [matrix[i+1][j], matrix[i+1][j+1]]]
            if box not in answer:
                answer.append(box)

    return len(answer)

# def differentSquares2(matrix):
#     answer = set()
#     for i in range(len(matrix)-1):
#         for j in range(len(matrix[0])-1):
#             box = (matrix[i][j], matrix[i][j+1],
#                    matrix[i+1][j], matrix[i+1][j+1])
#             answer.add(box)

#     return len(answer)


print(differentSquares([[1, 2, 1],
                        [2, 2, 2],
                        [2, 2, 2],
                        [1, 2, 3],
                        [2, 2, 1]]))  # 6
