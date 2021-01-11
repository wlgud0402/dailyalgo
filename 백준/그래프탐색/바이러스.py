import sys

# sys.stdin = open('바이러스.txt')
node_count = int(input())
line_count = int(input())

graph = {}
for i in range(1, node_count+1):
    graph[i] = []

for _ in range(line_count):
    start, end = map(int, input().split(" "))
    graph[start].append(end)
    graph[start].sort(reverse=True)

visited = set()
stack = []
stack.append(1)
visited.add(1)

dfs = []

while len(stack) > 0:
    curr = stack.pop()
    dfs.append(str(curr))
    print(dfs)
    for adj in graph[curr]:
        if adj not in visited:
            stack.append(adj)
            visited.add(adj)

print(len(dfs)-1)
