def solution(nums, div):
    answer = []
    for num in nums:
        if num % div == 0:
            answer.append(num)
    
    
    if len(answer) == 0:
        return [-1]
    else:
        answer.sort()
        return answer






print(solution([5,9,7,10], 5))
#출력 [5,10]