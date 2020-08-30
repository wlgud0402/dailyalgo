class Solution:
    def isPalindrome(self, string):
        string_alnum = "".join([s.lower() for s in string if s.isalnum()])
        
        # if string_alnum == string_alnum[::-1]:
        #     return True
        # else:
        #     return False
        return string_alnum == string_alnum[::-1]


solution = Solution()
print(solution.isPalindrome("A man, a plan, a canal: Panama"))
#true