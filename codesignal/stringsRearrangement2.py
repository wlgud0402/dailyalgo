# -*- coding: utf-8 -*-
import itertools


def stringsRearrangement(inputArray):
    nPr = list(itertools.permutations(inputArray, len(inputArray)))

    for array in nPr:
        flag = False
        diff_count = 0
        # array
        for i in range(len(array)-1):
            for j in range(len(array[0][0])):
                if diff_count >= 2:
                    break
                if array[i][j] != array[i+1][j]:
                    diff_count += 1

    if diff_count <= 1:
        return True


print(stringsRearrangement(["aba",
                            "bbb",
                            "bab"]))
