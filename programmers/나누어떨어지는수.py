numbers =[5,9,7,]

def solution(numbers, divisor):
    answer = []
    for number in numbers:
        if number % divisor == 0:
            answer.append(number)

    answer.sort()

    if answer:
        return answer
    else:
        return [-1]

print(solution([5, 9, 7, 10],5))   
print(solution([2, 36, 1, 3],1))  
print(solution([3,2,6],10))  
