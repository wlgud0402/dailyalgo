class Solution:
    def restoreString(self, s, orders):
        answer = list("*" * len(s))
        for i in range(len(orders)):
            answer[orders[i]] = s[i]
        return "".join(answer)



solution = Solution()
print(solution.restoreString("codeleet",[4,5,6,7,0,2,1,3]))