class Solution:
    def uniqueOccurrences(self, arr):
        count = {}
        for num in arr:
            if num not in count: #딕셔너리에 키값이 저장되있지 않으면 생성
                count[num] = 1
            else:
                count[num] += 1

        if len(count) == len(set(count.values())):
            return True
        else:
            return False




solution = Solution()
print(solution.uniqueOccurrences([1,2,2,1,1,3]))
        