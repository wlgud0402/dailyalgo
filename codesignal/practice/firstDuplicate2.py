import collections


def firstDuplicate(array):
    count = {}
    if len(array) == len(set(array)):
        return -1

    for i in range(len(array)):
        if array[i] in count:
            count[array[i]] += 1
            if count[array[i]] == 2:
                return array[i]
        else:
            count[array[i]] = 1


print(firstDuplicate([1, 1, 2, 2, 1]))  # 1
