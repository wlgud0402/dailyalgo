def solution(A):
    count = {}
    for num in A:
        if num not in count:
            count[num] = 0
        count[num] += 1
    for key, value in count.items():
        if value % 2 != 0:
            return key


print(solution([9, 3, 9, 3, 9, 7, 9]))#7