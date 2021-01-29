# the ice is melting down but effected by
# water count about surrounding ice

import sys

sys.stdin = open('빙산.txt')
row_count, col_count = map(int, sys.stdin.readline().split(" "))

matrix = []
for _ in range(row_count):
    row = list(map(int, sys.stdin.readline().split(" ")))
    matrix.append(row)

for i in range(row_count):
    print(matrix[i])
print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")

global day_count
day_count = 0
while True:
    visited = set()
    stack = []
    divide_count = 0
    melting_poing_speed = set()
    print("divide_count", divide_count)

    for i in range(row_count):
        for j in range(col_count):
            if (i, j) not in visited and matrix[i][j] != 0:
                for dr, dc in ((-1, 0), (0, 1), (1, 0), (0, -1)):
                    next_r = i + dr
                    next_c = j + dc

                    if(
                        0 <= next_r < row_count
                        and 0 <= next_c < col_count
                        and matrix[next_r][next_c] != 0
                        and (next_r, next_c) not in visited
                    ):
                        stack.append((i, j))
                        visited.add((i, j))
                        divide_count += 1

            while len(stack) > 0:
                print("stack:", stack)
                surround_water_count = 0
                r, c = stack.pop()

                for dr, dc in ((-1, 0), (0, 1), (1, 0), (0, -1)):
                    next_r = r + dr
                    next_c = c + dc

                    if(
                        0 <= next_r < row_count
                        and 0 <= next_c < col_count
                        and matrix[next_r][next_c] != 0
                        and (next_r, next_c) not in visited
                    ):
                        visited.add((next_r, next_c))
                        stack.append((next_r, next_c))
                        surround_water_count += 1
                        melting_poing_speed.add((r, c, surround_water_count))

    for r, c, surround_water_count in melting_poing_speed:
        print("r,c,surround_water_count", r, c, surround_water_count)
        if matrix[r][c] - surround_water_count > 0:
            matrix[r][c] -= surround_water_count
        else:
            matrix[r][c] = 0

    for i in range(row_count):
        print(matrix[i])
    print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")

    if divide_count == 0:
        print("div never gonna be bigger then 2")
        break

    day_count += 1
    if divide_count >= 2:
        # print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ", day_count)
        # for i in range(row_count):
        #     print(matrix[i])

        print("i should return day_count")
        break
