def solution(numbers):
    min_num = min(numbers)
    numbers.remove(min_num)
    
    if numbers:
        return numbers
    else:
        return -1




print(solution([4,3,2,1]))