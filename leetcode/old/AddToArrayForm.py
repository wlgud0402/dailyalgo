class Solution:
    def addToArrayForm(self, nums,plus):
        num = ""
        answer = []
        for i in range(len(nums)):
            num += str(nums[i])
        num = str(int(num) + plus)
        
        for n in num:
            answer.append(int(n))
        return answer
        

solution = Solution()
print(solution.addToArrayForm([1,2,0,0],34))