N, M, V = map(int, input().split())
matrix = [[0]*(N+1) for i in range(N+1)]
for i in range(M):
    a, b = map(int, input().split())
    matrix[a][b] = matrix[b][a] = 1
visit_list = [0]*(N+1)


def dfs(V):
    visit_list[V] = 1
    print(V)
    for i in range(1, N+1):
        if(visit_list[i] == 0 and matrix[V][i] == 1):
            dfs(i)


dfs(V)
# 4 5 1
# 1 2
# 1 3
# 1 4
# 2 4
# 3 4
