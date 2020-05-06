def solution(num):
    n=0
    while num != 1:
        if num %2 == 0:
            num = num/2
            n+=1
        else:
            num = (num*3)+1
            n+=1
    if n > 500:
        return -1
    else:
        return n

print(solution(6))

#최대 500번이므로 for i in range(500)
def collatz(num):
    for i in range(500):
        if num % 2 == 0:
            num = num /2
        else:
            num = (num*3)+1
        if num ==1 :
            return i+1
    return -1

print(collatz(6))

def collatz2(num):
    for i in range(500):
        num = num / 2 if num % 2 == 0 else num*3 + 1 
        if num == 1:
            return i + 1
    return -1
        