class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        insert_idx = 0
        flag = False
        for i, v in enumerate(nums):
            if v == target:
                return i

            if v > target:
                insert_idx = i
                flag = True

            if v < target:
                if not flag:
                    return 0
                if flag:
                    return insert_idx

        return 0


solution = Solution()
print(solution.searchInsert([1, 3, 5, 6], 5))
