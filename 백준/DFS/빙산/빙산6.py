# the ice is melting down but effected by
# water count about surrounding ice

import sys

sys.stdin = open('빙산.txt')
row_count, col_count = map(int, sys.stdin.readline().split(" "))

matrix = []
for _ in range(row_count):
    row = list(map(int, sys.stdin.readline().split(" ")))
    matrix.append(row)

ices = []
for i in range(row_count):
    for j in range(col_count):
        if matrix[i][j] != 0:
            ices.append((i, j))

global day_count
day_count = 0
flag = True
while flag:
    visited = set()
    stack = []
    divide_count = 0
    melting_point_speed = set()
    again = False

    for ice in ices:
        r, c = ice
        if not again:
            if ice not in visited and matrix[r][c] != 0:
                print("ice", ice)
                stack.append((r, c))
                visited.add((r, c))
                print("stack, visited added!!", stack, visited)

            while len(stack) > 0:
                surround_water_count = 0
                r, c = stack.pop()
                print(r, c, "popped!")
                divide_count += 1

                for dr, dc in ((-1, 0), (0, 1), (1, 0), (0, -1)):
                    next_r = r + dr
                    next_c = c + dc

                    if(
                        0 <= next_r < row_count
                        and 0 <= next_c < col_count
                        and matrix[next_r][next_c] != 0
                        and (next_r, next_c) not in visited
                    ):
                        stack.append((next_r, next_c))
                        visited.add((next_r, next_c))

                    if(
                        0 <= next_r < row_count
                        and 0 <= next_c < col_count
                        and matrix[next_r][next_c] == 0
                    ):
                        surround_water_count += 1
                melting_point_speed.add(
                    (r, c, surround_water_count))

    for r, c, surround_water_count in melting_point_speed:
        if matrix[r][c] - surround_water_count > 0:
            matrix[r][c] -= surround_water_count
        else:
            matrix[r][c] = 0
    again = True
    break

    for i in range(row_count):
        print(matrix[i])
    print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
    break
