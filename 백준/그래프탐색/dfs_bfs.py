import sys
from collections import deque

sys.stdin = open('dfs_bfs.txt')
N, M, start = map(int, input().split(" "))
graph = {}
for i in range(1, N+1):
    graph[i] = []
for _ in range(M):
    s, e = map(int, input().split(" "))
    graph[s].append(e)

for i in range(1, M):
    graph[i].sort()

print(graph)

visited = set()
stack = []
stack.append(start)
visited.add(start)

dfs = []

while len(stack) > 0:
    curr = stack.pop()
    dfs.append(str(curr))  # print(curr)
    for adj in graph[curr]:
        if adj not in visited:
            stack.append(adj)
            visited.add(adj)


visited = set()
queue = deque()
queue.append(start)
visited.add(start)

bfs = []

while len(queue) > 0:
    curr = queue.popleft()
    bfs.append(str(curr))
    for adj in graph[curr]:
        if adj not in visited:
            queue.append(adj)
            visited.add(adj)

print(" ".join(dfs))
print(" ".join(bfs))
