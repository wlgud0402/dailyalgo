numbers = [4,4,4,3,3]

def solution(numbers):
    answer = []
    answer.append(numbers[0])
    for i in range(1, len(numbers)):
        # if numbers[i] != numbers[i-1]:
        if numbers[i] != answer[-1]:
            answer.append(numbers[i])
    return answer

print(solution(numbers))
