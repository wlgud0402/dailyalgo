def extractEachKth(inputArray, k):
    remove_list = []
    for i, v in enumerate(inputArray):
        if (i+1) % k == 0:
            remove_list.append(v)

    remove_list = list(set(remove_list))

    while len(set(remove_list).intersection(inputArray)) != 0:
        for i, v in enumerate(inputArray):
            if v in remove_list:
                inputArray.remove(v)
    return inputArray


print(extractEachKth([1, 1, 1, 1, 1], 1))
