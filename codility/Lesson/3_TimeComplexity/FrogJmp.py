#당연하게도 Y가 매우 클경우 점프를 
#존나 많이 반복적으로 해야하기 때문에 시간초과
# def solution(X,Y,D):
#     count = 0
#     while X < Y:
#         X += D
#         count +=1 
#     return count
import math

def solution(X,Y,D):
    diff = Y - X
    jump = diff / D

    return math.ceil(jump)

print(solution(10,85,30))
