def solution(strings):
    bracket = {
        "(": ")",
        ")": "(",
        "[": "]",
        "]": "[",
        "{": "}",
        "}": "{"
    }

    stack = [strings[0]]
    for i in range(1, len(strings)):
        top = stack.pop()
        if bracket[top] == strings[i]:
            continue
        else:
            stack.append(top)
            stack.append(strings[i])

    if stack:
        return 0
    else:
        return 1


# print(solution("{[()()]}"))  # return 1
print(solution("([)()]"))  # return 0
