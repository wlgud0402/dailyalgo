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

print(matrix)
dangi_count = 0
ho_counts = []


def dfs(x, y, count):
    if x <= -1 or x >= dong_count or y <= -1 or y >= len(matrix[0]):
        return False

    if matrix[x][y] == 1:
        matrix[x][y] = 0
        print(count)
        count += 1

        dfs(x-1, y, count)
        dfs(x, y-1, count)
        dfs(x+1, y, count)
        dfs(x, y+1, count)

        ho_counts.append(count)
        return True

    return False


for i in range(dong_count):
    for j in range(len(matrix[0])):
        if dfs(i, j, 0) == True:
            dangi_count += 1


print(dangi_count, ho_counts)
# print(ho_counts)
