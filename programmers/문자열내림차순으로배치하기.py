def solution(s):
    s = [i for i in s]
    s.sort(reverse=True)
    s = ''.join(s)
    return s


def solution2(s):
    return ''.join(sorted(s, reverse=True))

# list(문자열) => ["문", "자", "열"]


print(solution("Zbcdefg"))
