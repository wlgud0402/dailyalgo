class Solution:
    def buildArray(self, target, n):    
        # if len(target) == 0:
        #     return []
        # result = [1]
        # action = ["Push"]
        # if target == result:
        #     return action        
        # for i in range(2, n + 1):
        #     if result[len(result) - 1] not in target:
        #         result.pop()
        #         action.append("Pop")
        #     result.append(i)
        #     action.append("Push")
        #     if target == result:
        #         return action

        output = [] 
        for i in range(1, n+1):
            if i > target[-1]:
                break
            if i in target:
                output.append("Push")
            else:
                output.append("Push")
                output.append("Pop")
        return output                    


            

solution=Solution()

print(solution.buildArray([1,3],3))
#출력 : ["Push","Push","Push"]
#Input: target = [1,3], n = 3
#Output: ["Push","Push","Pop","Push"]