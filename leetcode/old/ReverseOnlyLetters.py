class Solution:
    def reverseOnlyLetters(self, string):
        idx_string = []
        new_string = []
        for i, s in enumerate(string):
            if string[i].isalpha():
                new_string.append(s)
            else:
                idx_string.append([i,s])
                
        new_string = new_string[::-1]

        for v in idx_string:
            new_string.insert(v[0], v[1])
        
        return ''.join(new_string)

solution = Solution()
print(solution.reverseOnlyLetters("a-bC-dEf-ghIj"))