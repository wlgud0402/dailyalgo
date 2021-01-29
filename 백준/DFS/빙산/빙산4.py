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
    melting_point_speed = set()
    print("divide_count", divide_count)
    print("melting_point_speed reset!!", melting_point_speed)

    for i in range(row_count):
        for j in range(col_count):
            if (i, j) not in visited and matrix[i][j] != 0:
                stack.append((i, j))
                visited.add((i, j))
                divide_count += 1

            while len(stack) > 0:
                # print("stack:", stack)
                r, c = stack.pop()
                surround_water_count = 0
                # matrix[r][c] -= 1

                # for i in range(row_count):
                #     print(matrix[i])
                # print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")

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

                    if(
                        0 <= next_r < row_count
                        and 0 <= next_c < col_count
                        and matrix[next_r][next_c] == 0
                    ):
                        print("matrix[next_r][next_c]:", matrix[next_r]
                              [next_c], r, c, surround_water_count)
                        surround_water_count += 1
                if surround_water_count == 0:
                    melting_point_speed.add((r, c, 1))
                else:
                    melting_point_speed.add((r, c, surround_water_count))

                print("melting_point_and_speed added!!!!:", melting_point_speed)

    print(melting_point_speed)
    for r, c, surround_water_count in melting_point_speed:
        print("r,c,surround_water_count", r, c, surround_water_count)
        if matrix[r][c] - surround_water_count > 0:
            matrix[r][c] -= surround_water_count
        else:
            matrix[r][c] = 0

    for i in range(row_count):
        print(matrix[i])
    print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")

    if divide_count == 0:
        print("return 0")
        break

    day_count += 1
    if divide_count >= 2:
        print("i should return day_count")
        break
