# 1=> dfs

# first_graph = [
#     [1, 2],
#     [1, 3],
#     [1, 4],
#     [2, 4],
#     [3, 4]]  # start point => 1
# # node 3, line 5

# M = 5
# graph = [[] for i in range(M+1)]
# for i in range(len(first_graph)):
#     idx = first_graph[i][0]
#     graph[idx].append(first_graph[i][1])
# print(graph)

graph = [[], [2, 3, 4], [4], [4]]


def dfs(graph, v, visited):
    visited[v] = True
    print(v)
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


visited = [False] * 4
dfs(graph, 1, visited)
# 2=> bfs
