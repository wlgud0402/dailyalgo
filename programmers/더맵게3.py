import heapq


def solution(scoville, K):
    if min(scoville) >= K:
        return 0

    count = 0
    while min(scoville) < K:
        try:
            min_scoville = heapq.heappop(scoville)
            sec_scoville = heapq.heappop(scoville)

            mix = min_scoville + (sec_scoville * 2)
            heapq.heappush(scoville, mix)

            count += 1
            continue
        except:
            return -1
    return count


print(solution([5], 6))
