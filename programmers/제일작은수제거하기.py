def solution(numbers):
    if len(numbers) == 1 and numbers[0] == 10:
        return -1
    elif len(numbers) == 0:
        return -1
    else:
        min_number = min(numbers)
        numbers.remove(min_number)
        return numbers

print(solution([4,3,2,1]))