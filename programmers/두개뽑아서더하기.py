def solution(numbers):
    numbers.sort()
    answers = []
    for i in range(len(numbers)-1):
        for j in range(i+1, len(numbers)):
            print(i, j)
            answers.append(numbers[i] + numbers[j])
    answers = list(set(answers))
    answers.sort()
    return answers


print(solution([5, 0, 2, 7]))
