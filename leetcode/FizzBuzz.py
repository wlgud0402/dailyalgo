class Solution:
    def fizzBuzz(self, n):
        answer = []
        for i in range(1, n+1):
            if i == 1:
                answer.append(str(i))
                continue
            elif i % 15 == 0:
                answer.append("FizzBuzz")
                continue
            elif i % 3 == 0:
                answer.append("Fizz")
            elif i % 5 == 0:
                answer.append("Buzz")
            else:
                answer.append(str(i))
        return answer
            




solution = Solution()
print(solution.fizzBuzz(15))
        