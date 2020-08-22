class Solution:
    def isAnagram(self, big, small):
        big_hash = {}
        small_hash = {}
        for b in big:
            if b not in big_hash:
                big_hash[b] = 1
            else:
                big_hash[b] += 1

        for s in small:
            if s not in small_hash:
                small_hash[s] = 1
            else:
                small_hash[s] += 1

        big_hash = sorted(big_hash.items())
        small_hash = sorted(small_hash.items())
        
        if big_hash == small_hash:
            return True
        else:
            return False






solution = Solution()
print(solution.isAnagram("ab","a"))



        