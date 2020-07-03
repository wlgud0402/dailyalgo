def solution(n, words):
    said_word = words[0]

    said_words = ""

    for i in range(1, len(words)):
        if said_word[-1] != words[i][0] or words[i] in said_words:
            return "여기서 몇번째의 사람이 몇번차때 실수"
        else:
            said_words += ","
            said_words += words[i]
    return [0,0]


print(solution(3,["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))
