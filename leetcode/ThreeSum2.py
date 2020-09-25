class Solution:
    def checkPerfectNumber(self, num):
        answer = []
        if num % 2 == 0:
            num = num//2
            for i in range(1, num+1):
                if num % i == 0:
                    print(num, i)
                    answer.append(i)
            print(sum(answer), num*2)
        
        
solution = Solution()
print(solution.checkPerfectNumber(28))