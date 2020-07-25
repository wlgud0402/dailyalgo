import copy
class Solution:
    def backspaceCompare(self, S, T):

        new_S = list(copy.deepcopy(S))
        for i in range(len(S)):
            if S[i] == "#":
                # try:
                new_S.pop(i)
                #     new_S.pop(i-1)
                # except:
                #     new_S.pop(i)


        new_T = list(copy.deepcopy(T))
        for j in range(len(T)):
            if T[j] == "#":
                # try:
                new_T.pop(j)
                #     new_T.pop(j-1)
                # except:
                #     new_T.pop(j)

        return new_S ,new_T


solution = Solution()
# print(solution.backspaceCompare("ab#c","ad#c"))
# print(solution.backspaceCompare("ab##","c#d#"))


print(solution.backspaceCompare("a##c","#a#c" ))


# print(solution.backspaceCompare("a#c", "b" ))
        