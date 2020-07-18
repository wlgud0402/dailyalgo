class Solution:
    def findNumbers(self, nums):
        answer = []

        for num in nums:
            if len(str(num)) % 2 ==0:
                answer.append(num)

        print(answer)
        print(answer[0])
        return len(answer)                       











solution=Solution()
print(solution.findNumbers([555,901,482,1771]))
#결과 1,            ok