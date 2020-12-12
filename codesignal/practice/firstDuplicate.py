import collections
# 3이상인 경우도 생각해야한다.


def firstDuplicate(array):
    if len(array) == len(set(array)):
        return -1
    count = collections.Counter(array)
    idx = 0
    number = array[0]

    for i in range(1, len(array)):
        if array[i] == number:
            return array[i]

        if count[array[i]] >= 2:
            number = array[i]

    # if len(array) == len(set(array)):
    #     return False
    # duplicate = -1
    # for i in range(len(array)-1, 0, -1):
    #     if array[i] in array[:i]:
    #         duplicate = array[i]
    # return duplicate
print(firstDuplicate([2, 1, 3, 5, 3, 2]))  # 3
