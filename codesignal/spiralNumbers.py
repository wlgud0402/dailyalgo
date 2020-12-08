def spiralNumbers(n):
    matrix = [[0]*n for i in range(n)]
    direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]  # R , D, L, U
    dx = {
        "R": [0, 1],
        "L": [0, -1],
        "U": [-1, 0],
        "D": [1, 0],
    }
    print(matrix)

    idx = [0, 0]
    arrow = "R"
    visited = []
    for i in range(1, (n*n)+1):
        print(i)
        if arrow == "R":
            if idx not in visited and idx[1]+1 < n:
                print(idx)
                visited.append(idx)
                print(visited)
                idx = [idx[0], idx[1]+1]
    # print(idx, visited)
    # print(idx, visited)
    # if arrow == "R":
    #     if idx in visited:
    #         arrow = "D"
    #         idx[0] +=1
    #         visited.append(idx)


print(spiralNumbers(3))
# [[1,2,3],
# [8,9,4],
# [7,6,5]]

# [[1,2,3,4,5],
#  [16,17,18,19,6],
#  [15,24,25,20,7],
#  [14,23,22,21,8],
#  [13,12,11,10,9]]
