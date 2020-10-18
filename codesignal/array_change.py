def arrayChange(inputArray):
    answer = 0
    flag = True
    while flag:
        for i in range(0, len(inputArray)-1):
            if inputArray[i] >= inputArray[i+1]:
                inputArray[i+1] += 1
                answer += 1
                break

        compare = sorted(set(inputArray))
        if compare == inputArray:
            flag = False
            break

    return answer
    # answer = 0
    # for i in range(0, len(inputArray)-1):
    #     if inputArray[i] >= inputArray[i+1]:
    #         inputArray[i+1] += 1
    #         answer += 1

    # return inputArray


# print(arrayChange([1, 1, 1]))
# return 3 [1, 1+(1) , 1+(2)] => (1+2):3

print(arrayChange([-1000, 0, -2, 0]))
