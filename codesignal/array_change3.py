def arrayChange(inputArray):
    answer = 0
    while sorted(set(inputArray)) != inputArray:
        diff = 0
        for i in range(0, len(inputArray)-1):
            inputArray = inputArray
            if inputArray[i] >= inputArray[i+1]:
                old = inputArray[i+1]
                new = inputArray[i] + 1
                inputArray[i+1] = new
                diff = new - old
                answer += diff

            else:
                continue
    return answer


print(arrayChange([1, 1, 1]))
# return 3
