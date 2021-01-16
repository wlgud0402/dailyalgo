from collections import deque
import sys

sys.stdin = open("dfs_bfs.txt")
N, M, start = map(int, sys.stdin.readline().split(" "))
graph = {}

for _ in range(M):
    s, e = map(int, sys.stdin.readline().split(" "))

    if s not in graph:
        graph[s] = []
    if e not in graph:
        graph[e] = []

    graph[s].append(e)
    graph[e].append(s)

for i in range(1, M):
    graph[i].sort()

visited = set()
stack = []
stack.append(start)
visited.add(start)

dfs = []

while len(stack) > 0:
    curr = stack.pop()
    dfs.append(str(curr))
    for adj in graph[curr]:
        if adj not in visited:
            stack.append(adj)
            visited.add(adj)
            break

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
