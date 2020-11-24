def lineEncoding(s):
    count = 1
    string = s[0]
    answer = ""
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            count += 1
        else:
            if count == 1:
                answer += s[i]
            else:
                append = str(count) + s[i-1]
                print(append, i)
                answer += append
                count = 1
    return answer


print(lineEncoding("aabbbc"))  # 2a3bc
