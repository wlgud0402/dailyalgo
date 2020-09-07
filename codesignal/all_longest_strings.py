def allLongestStrings(inputArray):
    max_length = 0
    for i in range(len(inputArray)):
        if len(inputArray[i]) > max_length:
            max_length = len(inputArray[i])

    answer = [inputArray[i] for i in range(len(inputArray)) if len(inputArray[i]) == max_length]
    return answer



print(allLongestStrings(["aba", "aa", "ad", "vcd", "aba"]))
#["aba", "vcd", "aba"]