def firstDuplicate(array):
    duplicate = -1
    for i in range(len(array)-1, 0, -1):
        if array[i] in array[:i]:
            duplicate = array[i]

    return duplicate


print(firstDuplicate([2, 1, 3, 5, 3, 2]))  # 3
