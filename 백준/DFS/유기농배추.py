import sys

sys.stdin = open("유기농배추.txt")
M, N, K = map(int, sys.stdin.readline().split(" "))

# x, y?
veges = []
for _ in range(K):
    x, y = map(int, sys.stdin.readline().split(" "))
    veges.append([y, x])

print(veges)

stack = []
visited = set()
count = 0

matrix = [[0]*M for i in range(N)]
for vege in veges:
    matrix[vege[0]][vege[1]] = 1

print(matrix[0])
print(matrix[1])
print(matrix[2])
print(matrix[3])
print(matrix[4])
print(matrix[5])
print(matrix[6])
print(matrix[7])

print(veges)

for vege in veges:
    if matrix[vege[0]][vege[1]] == 1:
        stack.append(vege)
        visited.add((vege[0], vege[1]))

        while len(stack) > 0:
            print("now stack: ", stack)
            x, y = stack.pop()
            visited.add((x, y))
            print("visited_1", visited)
            print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
            print("first", x, y)
            print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
            matrix[x][y] = 0
            print(matrix[0])
            print(matrix[1])
            print(matrix[2])
            print(matrix[3])
            print(matrix[4])
            print(matrix[5])
            print(matrix[6])
            print(matrix[7])
            for dx, dy in ((-1, 0), (0, 1), (1, 0), (0, -1)):
                next_x = x + dx
                next_y = y + dy
                print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
                print("before", x, y)
                print("next", next_x, next_y)
                print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")

                if(
                    next_x >= 0
                    and next_x < N
                    and next_y >= 0
                    and next_y < M
                    and matrix[next_x][next_y] == 1
                    and (next_x, next_y) not in visited
                ):
                    visited.add((next_x, next_y))
                    print("visited_2", visited)
                    stack.append([next_x, next_y])
                    print("stack", stack)

                else:
                    print("can't go there: ", next_x, next_y)
        print("before count:", count)
        print("end while count +1")
        count += 1

print(count)
