
graph = [
    [1, 1, 0, 1, 0, 1, 1],
    [1, 1, 0, 0, 0, 1, 1],
    [0, 0, 1, 0, 0, 1, 1],
    [1, 0, 0, 0, 1, 0, 0],
    [1, 1, 1, 0, 0, 0, 1]
]
# 5


def dfs(x, y):
    if x <= -1 or x >= len(graph) or y <= -1 or y >= len(graph[0]):
        return False

    if graph[x][y] == 1:
        graph[x][y] = 0

        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        dfs(x-1, y-1)
        dfs(x-1, y+1)
        dfs(x+1, y-1)
        dfs(x+1, y+1)
        print(x, y)
        return True
    return False


result = 0
for i in range(len(graph)):
    for j in range(len(graph[0])):
        if dfs(i, j) == True:
            result += 1

print(result)


# def dfs(x, y, island):
#     visited = []
#     result = 0
#     for i in range(len(island)):
#         for j in range(len(island[0])):
#             # if i-1 < 0 or i+1 > len(island) or j-1 < 0 or j+1 > len(island[0]):
#             if i < 0 or i > len(island) or j < 0 or j > len(island[0]):
#                 print(i, j, "over")
#                 continue

#             if island[i][j] == 0:
#                 continue

#             print(island[i][j], "   :", i, j)
#             island[i][j] = 0

#             dfs(x-1, y, island)
#             dfs(x+1, y, island)
#             dfs(x, y-1, island)
#             dfs(x, y+1, island)
#             dfs(x-1, y-1, island)
#             dfs(x-1, y+1, island)
#             dfs(x+1, y-1, island)
#             dfs(x+1, y+1, island)
#             result += 1
#             print(result)


# dfs(0, 0, island)
