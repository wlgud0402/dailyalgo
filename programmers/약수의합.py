def solution(n):
    answer = 0
    for i in range(1, n+1):
        if n % i == 0:
            answer += i
    return answer


# return num + sum([i for i in range(1, (num // 2) + 1) if num % i == 0])
# 약수를 구하는 것이므로 반이상의 경우에는 볼 필요가 없어진다.
print(solution(12))
# 1,2,3,4,6,12  => 28
