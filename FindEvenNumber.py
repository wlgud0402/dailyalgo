class Solution:
    def findNumbers(self, nums):
        answer = 0
        for num in nums:
            if len(str(num)) % 2 == 0:
                answer += 1
        return answer

solution = Solution()
print(solution.findNumbers([12,345,2,6,7896]))
#출력 2