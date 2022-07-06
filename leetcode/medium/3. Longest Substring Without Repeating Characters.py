class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest_substring = ""
        max_len = 0
        for i in range(len(s)):
            new_longest_substring = longest_substring + s[i]
            if len(set(new_longest_substring)) == len(new_longest_substring):
                longest_substring = new_longest_substring
            else:
                longest_substring = new_longest_substring[1:]

            if len(longest_substring) > max_len:
                max_len = len(longest_substring)
        return max_len


solution = Solution()
print(solution.lengthOfLongestSubstring("bbbbb"))
