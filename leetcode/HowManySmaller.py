class Solution:
    def smallerNumbersThanCurrent(self, nums):
        answer = []
        
        for i in range(len(nums)):
            count = 0
            for j in range(len(nums)):
                if nums[i] > nums[j] and i != j:
                    count +=1
                else:
                    pass
            answer.append(count)

        return answer




solution = Solution()
print(solution.smallerNumbersThanCurrent([8,1,2,2,3]))