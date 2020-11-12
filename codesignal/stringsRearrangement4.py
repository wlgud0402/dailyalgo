import itertools


def stringsRearrangement(inputArray):
    nPr = list(set(itertools.permutations(inputArray, len(inputArray))))
    for array in nPr:
        flag = True
        for i in range(len(array)-1):
            diff_count = 0
            for j in range(len(array[0])):
                if array[i][j] != array[i+1][j]:
                    diff_count += 1
                    if diff_count >= 2:
                        flag = False
                        break

            if diff_count != 1:
                flag = False
                break

        if flag == True:
            return True

    if flag == True:
        return True
    else:
        return False
