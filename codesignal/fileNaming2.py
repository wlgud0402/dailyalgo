def fileNaming(names):
    answer = []
    count = {}
    for name in names:
        if name in count:
            count[name] += 1
            new = name+"("+str(count[name])+")"
            if new in count:
                while new in count:
                    count[name] += 1
                    new = name+"("+str(count[name])+")"
                answer.append(new)
                count[new] = 0
                continue
            answer.append(new)
            count[new] = 0
        else:
            answer.append(name)
            count[name] = 0
    print(count)
    return answer

    # answer = []
    # count = {}
    # for name in names:
    #     if name in count:

    #         count[name] += 1
    #         new = name+"("+str(count[name])+")"
    #         answer.append(new)
    #         count[new] = 0
    #     else:
    #         answer.append(name)
    #         count[name] = 0
    # print(count)
    # return answer


print(fileNaming(["doc", "doc", "image", "doc(1)", "doc"]))
# ["doc", "doc(1)", "image", "doc(1)(1)", "doc(2)"]
