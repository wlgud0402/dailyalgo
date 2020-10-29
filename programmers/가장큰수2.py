import itertools


def solution(numbers):
    numbers = [str(i) for i in numbers]
    combination = list(itertools.permutations(numbers, len(numbers)))
    print(combination)
    for i in range(len(combination)):
        combination[i] = ''.join(combination[i])

    combination = [int(i) for i in combination]
    return str(max(combination))


print(solution([3, 30, 34, 5, 9]))
# "6210"
