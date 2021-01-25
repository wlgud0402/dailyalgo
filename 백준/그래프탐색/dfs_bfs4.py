from collections import deque
import sys

sys.stdin = open("dfs_bfs.txt")
N, M, V = map(int, input().split(" "))

graph = {}
for i in range(1, N + 1):
    graph[i] = []
for _ in range(M):
    a, b = map(int, input().split(" "))
    graph[a].append(b)
    graph[b].append(a)

stack = []
stack.append(V)
visited = set()
visited.add(V)

dfs_results = []

while len(stack) > 0:
    curr = stack.pop()
    visited.add(curr)
    dfs_results.append(str(curr))
    for adj in sorted(graph[curr], reverse=True):
        if adj not in visited:
            visited.add(adj)
            stack.append(adj)

visited = set()
queue = deque()
queue.append(V)
visited.add(V)

bfs_results = []

while len(queue) > 0:
    curr = queue.popleft()
    visited.add(curr)
    bfs_results.append(str(curr))
    for adj in sorted(graph[curr], reverse=True):
        if adj not in visited:
            visited.add(adj)
            queue.append(adj)

print(" ".join(dfs_results))
print(" ".join(bfs_results))
