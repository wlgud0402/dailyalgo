def solution(number):
    answer = [n for n in str(number)]
    answer.sort()
    answer.reverse()
    answer = int(''.join(answer))
    return answer

print(solution(1236745))
