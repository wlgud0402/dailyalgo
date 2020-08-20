class Solution:
    def arrayPairSum(self, nums):
        sum_answer = 0
        pair = []
        nums.sort()

        for n in nums:
            pair.append(n)
            if len(pair) == 2:
                sum_answer += min(pair)
                pair = []
        return sum_answer
                
    def arrayPairSum2(self, nums):
        sum_answer = 0
        nums.sort()

        for i, n in enumerate(nums):
            #짝수번째만 계산
            if i % 2 == 0:
                sum_answer += n
        return sum_answer


solution = Solution()
print(solution.arrayPairSum([1,4,3,2]))