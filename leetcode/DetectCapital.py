class Solution:
    def detectCapitalUse(self, word):
        if word == word.lower():
            return True
        elif word == word.upper():
            return True
        elif word == word.capitalize():
            return True
        else:
            return False



solution = Solution()
print(solution.detectCapitalUse("flaG"))
#True
        