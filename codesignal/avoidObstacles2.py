def avoidObstacles(inputArray):
    inputArray.sort()
    for i in range(1, inputArray[-1]+2):
        flag = True
        jump = i
        for num in inputArray:
            if num % i == 0:
                flag = False
                break
        if flag:
            return i


# print(avoidObstacles([3, 5, 6, 7, 9]))
print(avoidObstacles([2, 3]))
