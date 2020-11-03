def alphabeticShift(inputString):
    answer = ""
    for s in inputString:
        if ord(s)+1 >= 123:
            answer += "a"
            continue
        answer += chr(ord(s)+1)
    return answer


print(alphabeticShift("crazy"))
