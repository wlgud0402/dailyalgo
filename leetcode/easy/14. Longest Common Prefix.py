class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[-1]
        strs.sort(key=len)
        prefix = ""
        if len(strs[-1]) == 0:
            return prefix
        for i in range(len(strs[-1])):
            try:
                for j in range(len(strs)-1):
                    if strs[j][i] != strs[j+1][i]:
                        return prefix
                prefix += strs[j][i]
            except:
                return prefix
        return prefix
