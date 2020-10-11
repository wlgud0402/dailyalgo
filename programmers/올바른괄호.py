def solution(inputString):
    inputString = list(inputString)
    while True:
        left_idx = 0
        right_idx = 0
        for idx, s in enumerate(inputString):
            if s == "(":
                left_idx = idx

            if s == ")":
                right_idx = idx

                # print(left_idx, right_idx)
                # print(inputString[left_idx:right_idx+1])
                inputString[left_idx:right_idx+1] = ""
                print(inputString)
                break
        if len(inputString) == 0:
            return True
        if left_idx > right_idx:
            return False


# print(solution("(())()"))  # true
print(solution(")()("))  # false
