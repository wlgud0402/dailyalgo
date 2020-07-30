class Solution:
    def checkPerfectNumber(self, num):
        divide_nums = []
        for i in range(1 , (num + 1)):
            if num % i == 0 and num != i:
                divide_nums.append(i)

        if sum(divide_nums) == num:
            return True
        else:
            return False

solution = Solution()
print(solution.checkPerfectNumber(28))

# class Solution:
#     def checkPerfectNumber(self, num):
#         divide_num = 0
#         for i in range(1 , (num + 1)):
#             if num % i == 0 and num != i:
#                 divide_num += i

#         if divide_num == num:
#             return True
#         else:
#             return False

# solution = Solution()
# print(solution.checkPerfectNumber(28))
        