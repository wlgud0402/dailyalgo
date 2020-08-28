from collections import deque

def solution(scoville, K):
    scoville.sort()
    count = 0
    while min(scoville) < K:
        min_scoville = scoville.pop(0)
        sec_scoville = scoville.pop(0)

        mix = min_scoville + (sec_scoville * 2)
        scoville.append(mix)

        count += 1
        scoville.sort()
        continue
    return count


print(solution([1, 2, 3, 9, 10, 12],7))