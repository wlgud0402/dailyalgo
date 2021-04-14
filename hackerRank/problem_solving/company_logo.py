# 실패
from collections import Counter


def solution(s):
    count = Counter(s)
    count = count.most_common(3)
    sorted_count = sorted(count, key=lambda x: (-x[1], x[0]))
    # print(count)

    for key, value in sorted_count:
        print(key, value)


print(solution("qwertyuiopasdfghjklzxcvbnm"))

# a 1
# b 1
# c 1
