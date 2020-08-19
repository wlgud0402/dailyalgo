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



    def threeSum2(self, nums):
        nums.sort()
        answer = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if -(nums[i] + nums[j]) in nums[j+1:] and [nums[i], nums[j], -(nums[i] + nums[j])] not in answer:
                    answer.append([nums[i], nums[j], -(nums[i] + nums[j])])

        return answer

    def threeSum3(self, nums):
        nums.sort()
        answer = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if -(nums[i] + nums[j]) in nums[j+1:]:
                    possible = [nums[i], nums[j], -(nums[i] + nums[j])]
                    answer.append(possible)

        tuple_answer = set(map(tuple, answer))
        return [list(item) for item in tuple_answer]

solution = Solution()
print(solution.threeSum3([-1, 0, 1, 2, -1, -4]))
        