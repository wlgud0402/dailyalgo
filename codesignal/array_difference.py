def arrayMaximalAdjacentDifference(inputArray):
    answer = 0
    for i in range(len(inputArray)-1):
        if answer < abs(inputArray[i] - inputArray[i+1]):
            answer = abs(inputArray[i] - inputArray[i+1])

    return answer
