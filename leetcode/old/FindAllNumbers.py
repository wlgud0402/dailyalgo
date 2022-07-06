class Solution:
    def findDisappearedNumbers(self, nums):
        answer = []
        compare = [num for num in range(1, max(nums)+1)]

        for c in compare:
            if c not in nums:
                answer.append(c)
        return answer

        
solution = Solution()
print(solution.findDisappearedNumbers([1,2,3,4,6,7,8,9]))

