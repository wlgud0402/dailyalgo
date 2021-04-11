from collections import Counter


def solution(A):
    count = Counter(A)
    for key, value in count.items():
        if value == 1:
            return key


print(solution([9, 3, 9, 3, 9, 7, 9]))
