class Solution:
    def checkPerfectNumber(self, num):
        divide_nums = []
        for i in range(1 , (num)):
            if num % i == 0:
                divide_nums.append(i)

        if sum(divide_nums) == num:
            return True
        else:
            return False

    def checkPerfectNumber2(self, num):
        sum = 0
        for i in range(1 , int(num*0.5)):
            if num % i == 0:
                sum += i

        return sum == int(num*0.5)

    def checkPerfectNumber3(self, num):
        sum = 0
        for i in range(1, (num//2)):
            if num % i == 0:
                sum += i
        return sum == (num//2)


solution = Solution()
print(solution.checkPerfectNumber(28))
print(solution.checkPerfectNumber2(28))
print(solution.checkPerfectNumber3(33550336))

