class Solution:
    def defangIPaddr(self, address):
        answer = ""
        for s in address:
            if s == ".":
                answer += "[.]"
            else:
                answer += s
            """
            if s != ".":
                answer += s
            else:
                answer += "[.]"
            """
        return answer

solution=Solution()
print(solution.defangIPaddr("1.1.1.1"))
        

# print("1.1.1.1".replace(".", "[.]"))