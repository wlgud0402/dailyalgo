class Solution:
    def threeSum(self, nums):
        answer = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if -(nums[i] + nums[j]) in nums[j+1:]:
                    possible = [nums[i], nums[j], -(nums[i] + nums[j])]
                    possible.sort()
                if possible not in answer:
                    answer.append(possible)
        
        return answer





solution = Solution()
print(solution.threeSum([-1, 0, 1, 2, -1, -4]))
        