import sys
from collections import deque

sys.stdin = open('단지번호붙이기.txt')
dong_count = int(input())

matrix = []
for _ in range(dong_count):
    row = []
    for c in input():
        row.append(int(c))
    matrix.append(row)


count = 2


def dfs(x, y):
    if x <= -1 or x >= dong_count or y <= -1 or y >= len(matrix[0]):
        return False

    global count
    if matrix[x][y] == 1:
        matrix[x][y] = count

        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)

        return True

    return False


dangi_count = 0
ho_counts = {}
for i in range(dong_count):
    for j in range(len(matrix[0])):
        if dfs(i, j) == True:
            ho_counts[count] = 0
            count += 1
            dangi_count += 1

for i in range(dong_count):
    for j in range(len(matrix[0])):
        if matrix[i][j] in ho_counts:
            ho_counts[matrix[i][j]] += 1

ho_count = list(ho_counts.values())
ho_count.sort()

print(dangi_count)
for i in range(len(ho_count)):
    print(ho_count[i])
