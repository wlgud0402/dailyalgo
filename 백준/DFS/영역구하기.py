import sys

sys.stdin = open("영역구하기.txt")
M, N, K = map(int, sys.stdin.readline().split(" "))

#row, col
matrix = []
for _ in range(M):
    row = [0] * N
    matrix.append(row)

for _ in range(K):
    start_col, start_row, end_col, end_row = map(
        int, sys.stdin.readline().split(" "))

    for i in range(M):
        for j in range(N):
            if start_row <= i < end_row and start_col <= j < end_col:
                matrix[i][j] = 1


visited = set()
stack = []
area_count = 0
block_counts = []

for i in range(M):
    for j in range(N):
        flag = True
        block_count = 0
        if matrix[i][j] == 0:
            visited.add((i, j))
            stack.append((i, j))
            area_count += 1

        while len(stack) > 0:
            flag = False
            row, col = stack.pop()
            matrix[row][col] = 1
            block_count += 1

            for dr, dc in ((-1, 0), (0, 1), (1, 0), (0, -1)):
                next_r = row + dr
                next_c = col + dc

                if(
                    0 <= next_r < M
                    and 0 <= next_c < N
                    and matrix[next_r][next_c] == 0
                    and (next_r, next_c) not in visited
                ):
                    stack.append((next_r, next_c))
                    visited.add((next_r, next_c))

        if not flag:
            block_counts.append(block_count)
block_counts.sort()
print(area_count)
for block in block_counts:
    print(block, end=' ')
