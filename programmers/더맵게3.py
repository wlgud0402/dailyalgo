import heapq


def solution(scoville, K):
    heap = []
    for num in scoville:
        heapq.heappush(heap, num)

    count = 0
    while heap[0] < K:
        try:
            min_scoville = heapq.heappop(heap)
            sec_scoville = heapq.heappop(heap)

            mix = min_scoville + (sec_scoville * 2)
            heapq.heappush(heap, mix)

            count += 1
            continue
        except:
            return -1
    return count


print(solution([1, 2, 3, 9, 10, 12], 7))
