import sys
from collections import deque

sys.stdin = open('test2.txt')
row_count, col_count = map(int, input().split(" "))
matrix = []
for _ in range(row_count):
    row = []
    for c in input():
        row.append(int(c))
    matrix.append(row)

visited = set()
visited.add((0, 0))
queue = deque()
queue.append([(0, 0), visited, 1])

while len(queue) > 0:
    poss, visited, count = queue.popleft()
    r, c = poss
    if r == row_count - 1 and c == col_count - 1:
        print(count)

    for dr, dc in ((-1, 0), (0, 1), (1, 0), (0, -1)):
        next_r = r + dr
        next_c = c + dc
        if(
            next_r >= 0
            and next_r < row_count
            and next_c >= 0
            and next_c < col_count
            and matrix[next_r][next_c] == 1
            and (next_r, next_c) not in visited
        ):
            _visited = set(visited)
            _visited.add((next_r, next_c))
            queue.append([(next_r, next_c), _visited, count + 1])
