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

print(ices)

global day_count
day_count = 0
flag = True
while flag:
    visited = set()
    stack = []
    divide_count = 0
    melting_point_speed = set()

    if divide_count >= 2:
        flag = False
        break

    for ice in ices:
        r, c = ice
        if ice not in visited and matrix[r][c] != 0:
            stack.append((r, c))
            visited.add((r, c))

        while len(stack) > 0:
            surround_water_count = 0
            r, c = stack.pop()
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

    for i in range(row_count):
        print(matrix[i])
    print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")

    if divide_count == 0:
        print(0)
        break

    if not flag and divide_count >= 2:
        print(day_count)
        break
    day_count += 1

# global day_count
# day_count = 0
# flag = True
# while flag:
#     visited = set()
#     stack = []
#     divide_count = 0
#     melting_poing_speed = set()

#     for i in range(row_count):
#         if divide_count >= 2:
#             flag = False
#             break

#         for j in range(col_count):
#             if (i, j) not in visited and matrix[i][j] != 0:
#                 stack.append((i, j))
#                 visited.add((i, j))
#                 divide_count += 1

#                 while len(stack) > 0:
#                     surround_water_count = 0
#                     r, c = stack.pop()

#                     for dr, dc in ((-1, 0), (0, 1), (1, 0), (0, -1)):
#                         next_r = r + dr
#                         next_c = c + dc

    #     if(
    #         0 <= next_r < row_count
    #         and 0 <= next_c < col_count
    #         and matrix[next_r][next_c] != 0
    #         and (next_r, next_c) not in visited
    #     ):
    #         visited.add((next_r, next_c))
    #         stack.append((next_r, next_c))

    #     if(
    #         0 <= next_r < row_count
    #         and 0 <= next_c < col_count
    #         and matrix[next_r][next_c] == 0
    #     ):
    #         surround_water_count += 1
    # melting_poing_speed.add(
    #     (r, c, surround_water_count))

    # for r, c, surround_water_count in melting_poing_speed:
    #     if matrix[r][c] - surround_water_count > 0:
    #         matrix[r][c] -= surround_water_count
    #     else:
    #         matrix[r][c] = 0

    # if divide_count == 0:
    #     print(0)
    #     break

    # if not flag and divide_count >= 2:
    #     print(day_count)
    #     break
    # day_count += 1
