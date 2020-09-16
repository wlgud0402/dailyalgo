import math
def solution(number):
    if math.sqrt(number) == round(math.sqrt(number)):
        return int((math.sqrt(number)+1) * (math.sqrt(number)+1))
    else:
        return -1



print(solution(81))
#=> 144