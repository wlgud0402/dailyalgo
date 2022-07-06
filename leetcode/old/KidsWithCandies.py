class Solution:
    def kidsWithCandies(self, candies, extraCandies):
        max_candy = max(candies)
        answer = []
        for candy in candies:
            if max_candy <= candy + extraCandies:
                answer.append(True)
            else:
                answer.append(False)
        
        return answer
            




solution = Solution()
print(solution.kidsWithCandies([4,2,1,1,2],1))
#treu true true false true
        