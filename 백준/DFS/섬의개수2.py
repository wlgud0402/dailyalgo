import sys

sys.stdin = open('섬의개수.txt')

col_count, row_count = map(int, sys.stdin.readline().split(" "))

matrix = []
for _ in range(row_count):
    row = list(map(int, sys.stdin.readline().split(" ")))
    matrix.append(row)

stack = []
visited = set()
count = 0

for i in range(row_count):
    for j in range(col_count):
        if matrix[i][j] == 1:
            count += 1
            visited.add((i, j))
            stack.append((i, j))

        while len(stack) > 0:
            r, c = stack.pop()
            matrix[r][c] = 0

            for dr, dc in ((-1, 0), (0, 1), (1, 0), (0, -1), (-1, -1), (1, 1), (1, -1), (-1, 1)):
                next_r = r + dr
                next_c = c + dc

                if(
                    0 <= next_r < row_count
                    and 0 <= next_c < col_count
                    and matrix[next_r][next_c] == 1
                    and (next_r, next_c) not in visited
                ):
                    stack.append((next_r, next_c))
                    visited.add((next_r, next_c))

print(count)
