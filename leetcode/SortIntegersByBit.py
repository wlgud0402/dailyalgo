# class Solution:
#     def sortByBits(self, nums):
#         new_arr = []
#         for num in nums:
#             if num == 0:
#                 new_arr.append(0)
#             else:
#                 bin_num = bin(num)
#                 new_arr.append(bin_num)
        
        
#         last_arr = []
#         for new_num in new_arr:
#             if new_num == 0:
#                 continue

#             print(new_num.count('1'))


#         # answer = []
#         # for num in new_arr:
#         #     if num == 0 :
#         #         answer.append(0)
#         #     else:
#         #         num_ten = int(num, 2)
#         #         answer.append(num_ten)
#         # return answer





# solution = Solution()
# print(solution.sortByBits([0,1,2,3,41,5,6,7,8]))

# class Solution:
#     def sortByBits(self, arr):
#         result = [(bin(num).count('1'), num) for num in arr]
#         result.sort()
#         return [i[1] for i in result]

class Solution:
    def sortByBits(self, arr):
        result = [(bin(num).count('1'), num) for num in arr]
        result.sort()
        return [i[1] for i in result]




solution = Solution()
print(solution.sortByBits([0,1,2,3,4,5,6,7]))

        