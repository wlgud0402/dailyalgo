def solution(n, computers):
    graph = {}
    for i in range(n):
        graph[i+1] = []
        for j, v in enumerate(computers[i]):
            if i != j and v != 0:
                graph[i+1].append(j + 1)

    # print(graph)
    visited = set()
    stack = []
    count = 0
    for i in range(1, len(graph)+1):
        # print("i", i)
        if len(graph[i]) == 0:
            # print("none", i, graph[i])
            count += 1
            visited.add(i)
            continue

        if i not in visited:
            visited.add(i)
            stack.append(i)
            count += 1

        while len(stack) > 0:
            curr = stack.pop()
            # print("curr", curr)
            for adj in graph[curr]:
                if adj not in visited:
                    stack.append(adj)
                    visited.add(adj)

    return count


print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))  # 2
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))  # 1
