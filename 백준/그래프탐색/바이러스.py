# def solution()
from collections import deque

graph = [[1, 2],
         [2, 3],
         [1, 5],
         [5, 2],
         [5, 6],
         [4, 7]]


sorted_graph = sorted(graph)
print(sorted_graph)

start_links = []
for linked in sorted_graph:
    if linked[0] == 1:
        start_links.append(linked)
print(start_links)


# def dfs(x,y):
#     if graph[x][0] != 0:
#         graph[x][0] = 0

#         dfs(graph[x][1], graph[x])


# def bfs(graph, start, visited):
#     queue = deque([start])
#     visited[start] = True

#     while queue:
#         v = queue.popleft()
#         print(v, end=' ')

#         if not visited[]

# # 7 computer
# # 6 line
# visited = [False] * 7
# bfs(graph, 1, visited)
