def solution(s):
    if len(s) %2 == 0 :
        i = len(s) // 2
        return s[i-1:i+1]
    else:
        i = len(s) // 2
        return s[i]


print(solution("abcde"))

print(solution("qwer"))