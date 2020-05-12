import math

def solution(number):
    x = math.sqrt(number)
    if x >= 0 and x - int(x) == 0:
        return int((x+1)*(x+1))
    else:
        return -1

print(solution(3))