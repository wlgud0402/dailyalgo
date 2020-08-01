def solution(nums):
    answer = [int(num) for num in str(nums)]
    answer.reverse()
    return answer

print(solution(12345))