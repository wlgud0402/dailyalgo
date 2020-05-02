def solution(x, n):
    answer = []
    i=1
    for i in range(1, n+1):
        y = x*i
        answer.append(y)
    return answer

solution(2,5)
