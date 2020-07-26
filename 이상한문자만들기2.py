def solution(s):
    words = s.split(" ")
    print(words)
    
    answer = []
    for word in words:
        word = list(word)
        for i in range(len(word)):
            if i % 2 == 0:
                word[i] = word[i].upper()
            else:
                word[i] = word[i].lower()
        word = "".join(word)
        answer.append(word)

    answer = " ".join(answer)
    return answer

print(solution("try hello     world"))
#TrY HeLlO WoRlD
