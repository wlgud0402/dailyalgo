class Solution:
    #No stack
    def dailyTemperatures(self, T):
        max_num = max(T)
        answer = []
        for i in range(len(T)):
            if T[i] == max_num:
                answer.append(0)
                continue
            flag = True
            for j in range(i+1, len(T)):
                if T[i] < T[j]:
                    answer.append(j-i)
                    flag = False
                    break  
            if flag:
                answer.append(0)
            
        return answer




solution = Solution()
print(solution.dailyTemperatures([71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71]))
        