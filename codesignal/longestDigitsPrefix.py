def longestDigitsPrefix(inputString):
    answer = ""
    for i in range(len(inputString)):
        try:
            num = int(inputString[i])
            answer += inputString[i]
        except:
            return answer

    return answer


print(longestDigitsPrefix("0123456789"))  # "123"
