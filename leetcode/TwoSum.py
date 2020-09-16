class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i-1, 0-1 ,-1):
                if nums[i] + nums[j] == target:
                    return [j,i]


solution=Solution()

print(solution.twoSum([2, 7, 11, 15],9))