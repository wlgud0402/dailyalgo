import itertools


def stringsRearrangement(inputArray):
    nPr = list(itertools.permutations(inputArray, len(inputArray)))

    for array in nPr:
        flag = True
        for i in range(len(array)-1):
            diff_count = 0
            if flag:
                for j in range(len(array[0][0])):
                    if diff_count >= 2:
                        flag = False
                        break

                    if array[i][j] != array[i+1][j]:
                        diff_count += 1
            else:
                break

        if flag:
            return True
        else:
            return False

    # for array in nPr:
    #     flag = True
    #     for i in range(len(array)-1):
    #         diff_count = 0
    #         if flag:
    #             for j in range(len(array[0][0])):
    #                 if diff_count >= 2:
    #                     flag = False
    #                     break

    #                 if array[i][j] == array[i+1]:
    #                     continue
    #                 else:
    #                     diff_count += 1
    #         else:
    #             break

    #     if flag:
    #         return True
    #     else:
    #         return False


print(stringsRearrangement(["ab", "bb", "aa"]))
