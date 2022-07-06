class Solution:
    def findNumbers(self, nums):
        # return len([num for num in nums if len(str(num)) % 2 == 0])
        answer = 0
        for num in nums:
            if len(str(num)) % 2 == 0:
                answer += 1
        return answer

solution = Solution()
print(solution.findNumbers([12,345,2,6,7896]))
#출력 2

b = [1,2,3,4,5,6,7,8,9,10]

# [맵  for   필터]

# print([n + 10 for n in b if n % 2 == 0])

