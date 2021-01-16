import sys

sys.stdin = open('연결요소의개수.txt')
N, M = map(int, sys.stdin.readline().split(" "))
graph = {}
for i in range(1, N+1):
    graph[i] = []

for _ in range(M):
    s, e = map(int, input().split(" "))
    graph[s].append(e)
    graph[e].append(s)

for i in range(1, N+1):
    graph[i].sort()

print(graph)
count = 0
visited = set()
stack = []

for i in range(1, N+1):
    if i not in visited:
        stack.append(i)
        visited.add(i)

        while len(stack) > 0:
            curr = stack.pop()
            print(curr)
            for adj in graph[curr]:
                if adj not in visited:
                    stack.append(adj)
                    visited.add(adj)

        count += 1
print("count: ", count)
