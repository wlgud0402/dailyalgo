# -*- coding: utf-8 -*-
# def arrayMaxConsecutiveSum(inputArray, k):
#     max_sum = 0
#     for i in range((len(inputArray)+1)-k):
#         new_sum = sum(inputArray[i:i+k])
#         if max_sum <= new_sum:
#             max_sum = new_sum

#     return max_sum

# sum을 만들기 위해 계속 슬라이싱을 시도하지 않음 =>
# k개가 합쳐진 max_sum 에서 다음번째 수를 더하고 첫번째 원소의 수를 빼서 새로운 new_sum을 만들고 이를 max_sum과 비교해서 더 크다면 갱신
def arrayMaxConsecutiveSum(inputArray, k):
    max_sum = sum(inputArray[0:k])
    l = len(inputArray)
    last_v = max_sum
    for i in range(k, l):
        last_v = last_v+inputArray[i]-inputArray[i-k]
        if max_sum < last_v:
            max_sum = last_v
    return max_sum


print(arrayMaxConsecutiveSum([2, 3, 5, 1, 6], 2))  # 8
