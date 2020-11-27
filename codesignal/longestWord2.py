def longestWord(text):
    text = text.split()
    text = [list(i) for i in text]
    for i in range(len(text)):
        for s in text[i]:
            if s.isalpha():
                continue
            else:
                text[i].remove(s)

    print(text)


print(longestWord("Ready, steady, go!"))
