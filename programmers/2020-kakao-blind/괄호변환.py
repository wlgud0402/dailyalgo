def divide(will_divide_strings):
    bars = {}
    bars["("] = 0
    bars[")"] = 0

    for i, s in enumerate(will_divide_strings):
        bars[s] += 1
        if bars["("] == bars[")"] and \
                bars["("] != 0 and bars[")"] != 0:
            return will_divide_strings[:i+1], will_divide_strings[i+1:]


def is_right(partition):
    stack = []
    stack.append(partition[0])

    for i in range(1, len(partition)):
        top = stack.pop()
        if top != partition[i]:
            continue
        else:
            stack.append(top)
            stack.apend(partition[i])


def solution(strings):
    # 1번 조건
    if strings == "":
        return ""

    right_strings = ""
    while len(right_strings) != len(strings):
        u, v = divide(strings)
        return u, v


print(solution("()))((()"))  # "()(())()"
# ')(' => '()'
# 제거됨')('
