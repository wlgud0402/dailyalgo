import copy

class Solution:
    def rotateString(self, A, B):
        if len(A) == 0 and len(B) == 0:
            print("A: ",A , "B: ",B)
            return True

        A_copy = copy.deepcopy(A)
        posible_A = []

        for i in range(len(A)):
            A_copy += A[i]
            A_copy = A_copy[1:]

            posible_A.append(A_copy)

        if B in posible_A:
            return True
        else:
            return False
        
        
solution = Solution()
print(solution.rotateString("","a"))

print()

print(solution.rotateString("",""))

print()


print(solution.rotateString("abcde","cdeab"))
#true


print()


print(solution.rotateString("abcde","abced"))
#false
        