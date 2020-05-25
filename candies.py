class Solution:
    def kidsWithCandies(self, candies, extraCandies):
        answer = [] #true/false만 들어가는 리스트
        large = max(candies)

        for kid in candies:
            if kid + extraCandies < large:
                answer.append(False)
            else:
                answer.append(True)
        return answer



solution=Solution()

print(solution.kidsWithCandies([4,2,1,1,2],1))
#output [true, false, false, false, false]