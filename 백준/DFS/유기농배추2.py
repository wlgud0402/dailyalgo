T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split(" "))
    veges = []
    for _ in range(K):
        x, y = map(int, input().split(" "))
        veges.append([y, x])

        stack = []
        visited = set()
        count = 0

    matrix = [[0]*M for i in range(N)]
    for vege in veges:
        matrix[vege[0]][vege[1]] = 1

    for vege in veges:
        if matrix[vege[0]][vege[1]] == 1:
            stack.append(vege)
            visited.add((vege[0], vege[1]))

            while len(stack) > 0:
                x, y = stack.pop()
                visited.add((x, y))
                matrix[x][y] = 0
                for dx, dy in ((-1, 0), (0, 1), (1, 0), (0, -1)):
                    next_x = x + dx
                    next_y = y + dy

                    if(
                        next_x >= 0
                        and next_x < N
                        and next_y >= 0
                        and next_y < M
                        and matrix[next_x][next_y] == 1
                        and (next_x, next_y) not in visited
                    ):
                        visited.add((next_x, next_y))
                        stack.append([next_x, next_y])
            count += 1

    print(count)
