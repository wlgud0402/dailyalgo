class Solution:
    def createTargetArray(self, nums, index):
        answer = []
        for i in range(len(index)):
            idx = index[i]
            answer.insert(idx, nums[i])
        
        return answer






solution = Solution()
print(solution.createTargetArray([0,1,2,3,4], [0,1,2,2,1]))