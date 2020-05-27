class Solution:
    def uniqueOccurrences(self, arr):
        count = {}
        for num in arr:
            try: 
                count[num] += 1
            except:
                count[num] = 1
        if len(list(count.values())) == len(set((count.values()))):
            return True
        else:
            return False



solution=Solution()

print(solution.uniqueOccurrences([-3,0,1,-3,1,1,1,-3,10,0]))        