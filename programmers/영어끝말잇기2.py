def solution(n, words):
    said_words = [words[0]]
    for i in range(1, len(words)):
        if words[i] in said_words:
            return [(i % n)+1, (i//n)+1]
        if said_words[-1][-1] == words[i][0]:
            said_words.append(words[i])
        else:
            return [(i % n)+1, (i//n)+1]
    return [0, 0]


print(solution(2, ["hello", "one", "even", "never", "now", "world", "draw"]))
