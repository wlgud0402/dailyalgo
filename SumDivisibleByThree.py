from itertools import chain, combinations

class Solution:
    def maxSumDivThree(self, nums):
        else_sum_num = 0

        sum_num = sum(nums)
        if sum_num % 3 == 0:
            return sum_num
        else:
            possible_nums =  chain.from_iterable(combinations(nums, r) for r in range(len(nums) + 1))
            possible_nums = list(possible_nums)
            for i in range(len(possible_nums)):
                if sum(possible_nums[i])%3 == 0 and else_sum_num < sum(possible_nums[i]):
                    else_sum_num = sum(possible_nums[i])
            return else_sum_num  

             

# class Solution:
#     def maxSumDivThree(self, nums):
#         sum_num_list = []

#         sum_num = sum(nums)
#         if sum_num % 3 == 0:
#             return sum_num
#         else:
            

solution = Solution()
# # print(solution.maxSumDivThree([3,6,5,1,8]))
# # print(solution.maxSumDivThree([4]))
print(solution.maxSumDivThree([2,6,2,2,7]))

# from itertools import combinations

# l = ["x", "y", "z", ]

# def powerset(items):
#     combo = []
#     for r in range(len(items) + 1):
#         #use a list to coerce a actual list from the combinations generator
#         combo.append(list(combinations(items,r)))
#     return combo

# l_powerset = powerset(l)

# for i, item in enumerate(l_powerset):
#     print("All sets of length ", i)
#     print(item)

        


