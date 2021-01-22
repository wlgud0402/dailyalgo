import sys
from collections import deque

sys.stdin = open('토마토.txt')
col_count, row_count = map(int, sys.stdin.readline().split(" "))

matrix = []
for _ in range(row_count):
    row = list(map(int, sys.stdin.readline().split(" ")))
    matrix.append(row)

queue = deque()
visited = set()
need_to_fill = 0
day = 0

# go to remove
for i in range(len(matrix)):
    print(matrix[i])

for i in range(row_count):
    for j in range(col_count):
        if matrix[i][j] == 1:
            queue.append((i, j))
            visited.add((i, j))

        if matrix[i][j] != -1:
            need_to_fill += 1

print(queue)
print(visited)
print(need_to_fill)

while len(queue) > 0:
    day += 1
    print(queue)
    r, c = queue.popleft()
    matrix[r][c] = 1
    print(matrix[0])
    print(matrix[1])
    print(matrix[2])
    print(matrix[3])

    for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        next_r = dr + r
        next_c = dc + c

        if(
            0 <= next_r < row_count
            and 0 <= next_c < col_count
            and matrix[next_r][next_c] == 0
            and (next_r, next_c) not in visited
        ):
            queue.append((next_r, next_c))
            visited.add((next_r, next_c))
            print("adddded")
            print("added queue", queue)

if len(visited) == need_to_fill:
    print(day)
else:
    print(-1)
