def extractEachKth(inputArray, k):
    new_array = [v for i, v in enumerate(inputArray) if (i+1) % k != 0]
    return new_array


print(extractEachKth([5, 7, 11, 4, 10, -9, -1, 5, -2, 1, 11, -3, 4, 4, -3], 3))
#[5, 7, 4, 10, -1, 5, 1, 11, 4, 4]
