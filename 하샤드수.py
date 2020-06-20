#하샤드 수인가 구하는 알고리즘
def hashad(x):
    numbers = list(map(int, list(str(x))))
    answer = sum(numbers)
    if x % answer == 0:
        answer = True
    else:
        answer = False

    return answer
    

print(hashad(12))

def average(arr):
    average = sum(arr) / len(arr)
    
    return average
