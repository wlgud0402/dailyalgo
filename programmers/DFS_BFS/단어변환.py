def solution(begin, target, words):
    if target not in words:
        return

    visited = set()
    stack = []
    lord = []

    for word in words:
        count = 0
        for i in range(len(word)):
            if word[i] == begin[i]:
                continue
            else:
                count += 1

        if count == 1:
            stack.append(word)

    while len(stack) > 0:
        point = stack.pop()

        pass


print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))  # 4
# hit -> hot -> dot -> dog -> cog
