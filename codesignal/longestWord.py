def longestWord(text):
    text = [i for i in text if i.isalpha() or i == " "]
    words = ''.join(text)
    start = 0
    end = 0
    answer = []
    print(words)
    for i in range(len(words)):
        if words[i] == " ":
            end = i
            answer.append(words[start:end])
            start = end+1

    answer.append(words[start:])

    max_len = [0, 0]
    for i in range(len(answer)):
        if len(answer[i]) > max_len[0]:
            max_len = [len(answer[i]), answer[i]]

    return max_len[1]
