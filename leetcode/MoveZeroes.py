class Solution:
    def moveZeroes(self, nums):
        for i in range(len(nums)):
            if nums[i] == 0:
                nums.remove(0)
                nums.append(0)
        return nums


solution = Solution()
print(solution.moveZeroes([0,1,0,3,12]))