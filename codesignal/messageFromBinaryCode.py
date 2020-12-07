def messageFromBinaryCode(code):
    split = []
    start_idx = 0
    for i in range(1, len(code)):
        if i % 8 == 0:
            split.append(code[start_idx:i])
            start_idx = i
    split.append(code[start_idx:])

    for i in range(len(split)):
        if split[i][0] and split[1] == "0":
            split[i][1] = "b"

        split[i] = chr(int(split[i], 2))

    answer = ''.join(split)
    return answer


print(messageFromBinaryCode("010010000110010101101100011011000110111100100001"))
