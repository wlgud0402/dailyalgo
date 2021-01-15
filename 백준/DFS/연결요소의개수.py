import sys
from collections import deque
import copy

sys.stdin = open('연결요소의개수.txt')
N, M = map(int, sys.stdin.readline().split(" "))
graph = {}
for i in range(1, N+1):
    graph[i] = []

for _ in range(M):
    s, e = map(int, input().split(" "))
    graph[s].append(e)
    graph[e].append(s)

for i in range(1, M):
    graph[i].sort()

print(graph)
count = 0
visited = set()
stack = []

print(list(graph.values())[0][0])

# while len(stack) > 0:
start = list(graph.values())[0][0]

# for _ in range(2*N):


# while len(stack) > 0:
#     curr = stack.pop()
#     dfs.append(str(curr))  # print(curr)
#     for adj in graph[curr]:
#         if adj not in visited:
#             stack.append(adj)
#             visited.add(adj)

#             graph[curr].pop(0)
#             break
