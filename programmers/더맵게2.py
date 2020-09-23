import heapq


def solution(scoville, K):
    count = 0
    while min(scoville) < K:
        if len(scoville) == 1:
            return -1

        min_scoville = heapq.heappop(scoville)
        sec_scoville = heapq.heappop(scoville)

        mix = min_scoville + (sec_scoville * 2)
        heapq.heappush(scoville, mix)

        count += 1
        continue
    return count


print(solution([1, 2, 3, 9, 10, 12], 7))

# h = [1, 2, 4, 6, 7, 8]
# heapq.heappush(h, 5)
# heapq.heappop(h)
# print(h)
