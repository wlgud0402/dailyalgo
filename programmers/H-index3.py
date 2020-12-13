def solution(citations):
    citations.sort()
    H = citations[len(citations)//2]
    # large = 0
    # small = 0
    for i in range(len(citations)):
        large = [i for i in citations if i >= H]
        small = [i for i in citations if i < H]

        if len(large) >= H and len(small) < H:
            return H
        else:
            H += 1
    return H


print(solution([3, 0, 6, 1, 5]))
# 3
