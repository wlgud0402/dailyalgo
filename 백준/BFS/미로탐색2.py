import sys
from collections import deque

sys.stdin = open('미로탐색.txt')
row_count, col_count = map(int, sys.stdin.readline().split(" "))

matrix = []
for _ in range(row_count):
    row = []
    for c in input():
        row.append(int(c))
    matrix.append(row)

print(matrix[0])
print(matrix[1])
print(matrix[2])
print(matrix[3])

visited = set()
visited.add((0, 0))
queue = deque()
queue.append((0, 0))

print()

while len(queue) > 0:
    row, col = queue.popleft()
    if row == row_count - 1 and col == col_count - 1:
        print(matrix[row][col])
        print(matrix[0])
        print(matrix[1])
        print(matrix[2])
        print(matrix[3])

    for dr, dc in ((-1, 0), (0, 1), (1, 0), (0, -1)):

        next_row = row + dr
        next_col = col + dc

        if(
            next_row >= 0
            and next_row < row_count
            and next_col >= 0
            and next_col < col_count
            and matrix[next_row][next_col] == 1
            and (next_row, next_col) not in visited
        ):
            visited.add((next_row, next_col))
            queue.append((next_row, next_col))
            matrix[next_row][next_col] = matrix[row][col] + 1
