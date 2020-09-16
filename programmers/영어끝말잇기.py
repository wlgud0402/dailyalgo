def solution(n, words):
    said_words = words[0]

    for i in range(1, len(words)):
        if said_words[-1] != words[i][0] or words[i] in said_words:
            return [(i%n)+1, (i//n)+1]
        else:
            said_words += ","
            said_words += words[i]
    return [0,0]  


print(solution(3,["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))

print()
print()

print(solution(5,["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]))

print()
print()

print(solution(2,["hello", "one", "even", "never", "now", "world", "draw"]))