class Solution:
    def reverse(self, x: int) -> int:
        answer = 0
        min = -2**31
        max = 2**31-1
        reversed = str(x)[::-1]

        if reversed[-1] == '-':
            answer = int('-'+reversed[:-1])
        else:
            answer = int(reversed)

        if min <= answer <= max:
            return answer
        else:
            return 0


solution = Solution()

print(solution.reverse(123))
