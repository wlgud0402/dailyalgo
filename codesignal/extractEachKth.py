def extractEachKth(inputArray, k):
    new_array = [i for i in inputArray if i % k != 0]
    return new_array


print(extractEachKth([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3))
