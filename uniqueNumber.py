class Solution:
    def uniqueOccurrences(self, arr):
        count = {}
        for num in arr:
            try:    #count딕트에 num을 키로 가지고 있는곳에 1을 추가해주는 것을 시도 BUT 없다면 이제 한개추가되는것 => 오류 => except문 실행
                count[num] += 1
            except:
                count[num] = 1
        if len(list(count.values())) == len(set((count.values()))):
            return True
        else:
            return False



solution=Solution()

print(solution.uniqueOccurrences([-3,0,1,-3,1,1,1,-3,10,0]))        