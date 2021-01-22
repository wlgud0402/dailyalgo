import sys
import copy

sys.stdin = open('안전영역.txt')

N = int(sys.stdin.readline())

matrix = []
for _ in range(N):
    row = list(map(int, sys.stdin.readline().split(" ")))
    matrix.append(row)

safe_area_counts = []
waterHeight = 0

while True:
    _matrix = copy.deepcopy(matrix)
    area_count = 0
    stack = []
    visited = set()

    for i in range(N):
        for j in range(N):
            if _matrix[i][j] > waterHeight:
                _matrix[i][j] = 0
            else:
                _matrix[i][j] = -1

    for i in range(N):
        for j in range(N):
            if _matrix[i][j] == 0:
                area_count += 1
                visited.add((i, j))
                stack.append((i, j))

            while len(stack) > 0:
                r, c = stack.pop()
                _matrix[r][c] = -1

                for dr, dc in ((-1, 0), (0, 1), (1, 0), (0, -1)):
                    next_r = r + dr
                    next_c = c + dc

                    if(
                        0 <= next_r < N
                        and 0 <= next_c < N
                        and _matrix[next_r][next_c] == 0
                        and (next_r, next_c) not in visited
                    ):
                        stack.append((next_r, next_c))
                        visited.add((next_r, next_c))

    safe_area_counts.append(area_count)
    waterHeight += 1
    if area_count == 0:
        flag = False
        break

print(max(safe_area_counts))
