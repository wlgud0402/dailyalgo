class Solution:
    def numberOfSteps (self, num):
        count = 0
        while num != 0:
            if num % 2 == 0:
                num = num // 2
                count+=1
            else:
                num -= 1
                count+=1
        
        return count




solution = Solution()
print(solution.numberOfSteps(14))