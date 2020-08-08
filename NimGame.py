class Solution:
    def canWinNim(self, n):
        if n % 4 == 0:
            return False
        else:
            return True


solution = Solution()
print(solution.canWinNim(5))