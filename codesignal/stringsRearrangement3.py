# -*- coding: utf-8 -*-
import itertools


def stringsRearrangement(inputArray):
    nPr = list(set(itertools.permutations(inputArray, len(inputArray))))
    print(nPr)
    for array in nPr:
        flag = True
        for i in range(len(array)-1):
            print(array)
            diff_count = 0
            for j in range(len(array[0])):
                if array[i][j] != array[i+1][j]:
                    print("diff", array[i][j], "!=", array[i+1][j])
                    diff_count += 1
                    if diff_count >= 2:
                        print("flag를 폴스로!")
                        flag = False
                        break
                else:
                    print(diff_count)

            if not flag:
                break
            if flag == True and diff_count == 1:
                continue

    if flag == True and diff_count == 1:
        return True
    else:
        return False


# print(stringsRearrangement(["aba",
#                             "bbb",
#                             "bab"]))
print(stringsRearrangement(["ab",
                            "bb",
                            "aa"]))
