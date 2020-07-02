def solution(n, words):
    table = {}
    
    for word in words:
        if word in table:
            table[word] += 1
        else:
            table[word] = 1
    
    for i in range(len(words)):
        print(words[i+1])
        if words[i+1].startswith(words[i][-1]) and table[words][i] == 1:
                print(i)
                print("1")
                continue
        try:
            if words[i+1].startswith(words[i][-1]) and table[words][i] == 1:
                print(i)
                print("1")
                continue

            if words[i+1] == 2:
                print("1")
                return ["{}번사람".format(i) , "{}번째에".fortat(i)]


            if not words[i+1].startswith(words[i][-1]):
                print("1")
                return ["{}번째의 값은 그전문자의 마지막으로 시작하지     않음".format]


        except:
            return [0, 0]


print(solution(3,["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))