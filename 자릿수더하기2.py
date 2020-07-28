def solution(nums):
    answer = 0
    for num in str(nums):
        answer += int(num)
    return answer

print(solution(123))