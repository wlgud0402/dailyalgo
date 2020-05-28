class Solution:
    def replaceElements(self, arr):
        new_arr = []
        for i in range(len(arr)):
            try:
                new_arr.append(max(arr[i+1:]))
            except:
                new_arr.append(-1)
        return new_arr
                


solution=Solution()

print(solution.replaceElements([17,18,5,4,6,1]))
#출력 : [18,6,6,6,1,-1]
