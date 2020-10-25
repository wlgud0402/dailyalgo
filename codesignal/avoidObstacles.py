def avoidObstacles(inputArray):
    inputArray.sort()
    for i in range(1, inputArray[0]):
        jump = i
