def arrayChange(inputArray):
    answer = 0
    while sorted(set(inputArray)) != inputArray:
        for i in range(0, len(inputArray)-1):
            if inputArray[i] >= inputArray[i+1]:
                inputArray[i+1] += 1
                answer += 1
                continue

    return answer


print(arrayChange([1, 1, 1]))
# return 3
