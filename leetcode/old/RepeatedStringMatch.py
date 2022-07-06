# import copy

# class Solution:
#     def repeatedStringMatch(self, A, B):
#         copied_A = copy.deepcopy(A)
#         answer = 1
#         for i in range(0,10000):
#             if B in copied_A:
#                 return answer
#             else:
#                 answer += 1
#                 copied_A = copied_A + A
                
#         return -1
        

# class Solution:
#     def repeatedStringMatch(self, A, B):
#         for i in range(0,10000):
#             if B in i * A:
#                 return i
                
#         return -1
import copy

class Solution:
    def repeatedStringMatch(self, A, B):
        copied_A = copy.deepcopy(A)
        count = 1
        while B not in copied_A:
            copied_A += A
            count += 1

            if len(copied_A) >= len(A) + len(B):
                break
        
        if B not in copied_A:
            return -1
        else:
            return count

solution = Solution()
print(solution.repeatedStringMatch("abcd","cdabcdab")) #3
print(solution.repeatedStringMatch("abc","cabcabca")) #4                    
print(solution.repeatedStringMatch("aaaaaaaaaaaaaaaaaaaaa","bacbacbac")) #-1



























# import copy

# class Solution:
#     def repeatedStringMatch(self, A, B):
#         copied_A = copy.deepcopy(A)
#         count = 1
#         while B not in copied_A:
#             copied_A += A
#             count += 1

#             if len(copied_A) >= len(A) + len(B):  # while len(copied_A)<=len(A)+len(B): # cause if that's not the case, B is never going to be in A
#                 print(copied_A , A, B)
#                 break
        
#         # if B not in copied_A:
#         #     return -1
#         # else:
#         #     return count
#         return -1 if B not in copied_A else count
