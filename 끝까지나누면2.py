#collatz 콜라츠 추측

def solution(num):
    count = 0
    while num != 1:
        if num % 2 == 0:
            num = num // 2
            count += 1
        else:
            num = (num * 3) + 1
            count +=1
    if count > 500:
        return -1
    else:
        return count











print(solution(6))
#결과 8