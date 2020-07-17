# class Solution:
#     def findLucky(self, nums):
#         count = {}
#         for num in nums:
#             if count[num]:
#                 count[num] += 1
#             else:
#                 count[num] = 1
        
#         for i in range(len(count)):
#             if 






# solution = Solution()
# print(solution.findLucky([2,2,3,4]))

# count = {1:6,2:8}

# print(count[1])



# print(set_counts[0])
# print(counts.count(1))


class Solution:
    def findLucky(self, nums):
        no_repeats = set(nums)
        no_repeats = list(no_repeats)

        lucky_num = 0
        for i in range(len(no_repeats)):
            if no_repeats[i] == nums.count(no_repeats[i]) and no_repeats[i] > lucky_num: 
                lucky_num = no_repeats[i]

        if lucky_num == 0:
            return -1
        else:
            return lucky_num


solution = Solution()
print(solution.findLucky([2,2,3,4]))

