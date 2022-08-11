class Solution:
    def isPalindrome(self, x: int) -> bool:
        string = [i for i in str(x)]
        if string == string[::-1]:
            return True
        else:
            return False
