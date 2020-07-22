import copy

class Solution:
    def duplicateZeros(self, arr):
        count = len(arr)
        new_arr = copy.deepcopy(arr)
        for i in range(count):
            if arr[i] == 0:
                new_arr.insert(i+1, 0)
        
        arr = new_arr[:count]
        print(arr)


solution = Solution()
print(solution.duplicateZeros([1,0,2,3,0,4,5,0]))
print(solution.duplicateZeros([1,2,3]))
print(solution.duplicateZeros([1,0,3,0,2,2,0]))

# => [1,0,0,2,3,0,0,4]





#리턴없이 원래 arr를 바꾸기
#원래 길이 초과할수 x