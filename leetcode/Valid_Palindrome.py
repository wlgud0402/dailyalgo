class Solution:
    def isPalindrome(self, string):
        string_alnum = "".join([s.lower() for s in string if s.isalnum()])
        return string_alnum == string_alnum[::-1]
        # if string_alnum == string_alnum[::-1]:
        #     return True
        # else:
        #     return False
        

        # mid = len(string_alnum) / 2
        # left = 0
        # while left < mid:
        #     right = len(string_alnum) - 1 - left
        #     if string_alnum[left] != string_alnum[right]:
        #         return False
        #     left += 1
        # return True


solution = Solution()
print(solution.isPalindrome("A man, a plan, a canal: Panama"))
#true