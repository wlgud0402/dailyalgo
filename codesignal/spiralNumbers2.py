def spiralNumbers(n):
    matrix = [[0]*n for i in range(n)]
    idx = [0, 0]
    arrow = "R"
    visited = []
    for i in range(1, (n*n)+1):
        matrix[idx[0]][idx[1]] = i
        visited.append(idx)
        if arrow == "R":
            if idx[1]+1 < n and [idx[0], idx[1]+1] not in visited:
                idx = [idx[0], idx[1]+1]
                continue
            else:
                arrow = "D"
                idx = [idx[0]+1, idx[1]]
                continue

        if arrow == "D":
            if idx[0]+1 < n and [idx[0]+1, idx[1]] not in visited:
                idx = [idx[0]+1, idx[1]]
                continue
            else:
                arrow = "L"
                idx = [idx[0], idx[1]-1]
                continue

        if arrow == "L":
            if idx[1]-1 > -1 and [idx[0], idx[1]-1] not in visited:
                idx = [idx[0], idx[1]-1]
                continue
            else:
                arrow = "U"
                idx = [idx[0]-1, idx[1]]
                continue

        if arrow == "U":
            if idx[0]-1 > -1 and [idx[0]-1, idx[1]] not in visited:
                idx = [idx[0]-1, idx[1]]
                continue
            else:
                arrow = "R"
                idx = [idx[0], idx[1]+1]
                continue
    return matrix

    # dx = {
    #     "R": [0, 1],
    #     "L": [0, -1],
    #     "U": [-1, 0],
    #     "D": [1, 0],
    # }


print(spiralNumbers(3))
