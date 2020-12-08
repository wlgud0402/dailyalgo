def messageFromBinaryCode(code):
    bundle = []
    start_idx = 0
    for i in range(1, len(code)):
        if i % 8 == 0:
            bundle.append(code[start_idx:i])
            start_idx = i
    bundle.append(code[start_idx:])
    for i in range(len(bundle)):
        bundle[i] = chr(int(bundle[i], 2))

    answer = ''.join(bundle)
    return answer


print(messageFromBinaryCode("010010000110010101101100011011000110111100100001"))
