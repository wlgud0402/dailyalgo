from heapq import heappush, heappop


def solution(n, k, enemy):
    if k >= len(enemy):
        return len(enemy)

    left_soilder_count = n
    pass_ticket = k

    heap = []
    for i, v in enumerate(enemy):
        heappush(heap, (-v, v, i))

    print(heappop(heap))
    print(heappop(heap))
    print(heappop(heap))
    prevent_count = 0

    answer = 0
    return answer
