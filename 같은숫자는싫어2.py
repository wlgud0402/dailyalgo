def solution(nums):
    answer = [nums[0]]
    for i in range(1,len(nums)):
        if nums[i] == answer[-1]:
            continue
        answer.append(nums[i])
    return answer


        
        







print(solution([1,1,3,3,0,1,1]))