import sys

sys.stdin = open('빙산.txt')
row_count, col_count = map(int, sys.stdin.readline().split(" "))

matrix = []
for _ in range(row_count):
    row = list(map(int, sys.stdin.readline().split(" ")))
    matrix.append(row)

# for i in range(len(matrix)):
#     print(matrix[i])

day_count = 0

flag = True
while flag:
    day_count += 1
    visited = set()
    stack = []
    divide_count = 0

    for i in range(row_count):
        for j in range(col_count):
            if matrix[i][j] != 0 and (i, j) not in visited:
                stack.append((i, j))
                visited.add((i, j))

            while len(stack) > 0:
                row, col = stack.pop()
                print(row, col, matrix[row][col])
                matrix[row][col] -= 1
                divide_count += 1
                for i in range(len(matrix)):
                    print(matrix[i])
                print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
                print("divide_count", divide_count)

                for dr, dc in ((-1, 0), (0, 1), (1, 0), (0, -1)):
                    next_r = row + dr
                    next_c = col + dc

                    if(
                        0 <= next_r < row_count
                        and 0 <= next_c < col_count
                        and matrix[next_r][next_c] != 0
                        and (next_r, next_c) not in visited
                    ):
                        stack.append((next_r, next_c))
                        visited.add((next_r, next_c))
            print("divide_count222", divide_count)

    if divide_count >= 2:
        print("디브카운트 오버!", divide_count)
        flag = False

print(day_count)
