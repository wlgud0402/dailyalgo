def solution(number):
    numbers = [int(n) for n in str(number)]
    answer = 0
    for number in numbers:
        answer += number
    return answer
    