import copy


def areSimilar(a, b):
    if a == b:
        return True

    for i in range(len(a)):
        for j in range(i+1, len(b)):
            print(i, j)
            copy_a = copy.deepcopy(a)
            copy_b = copy.deepcopy(b)

            copy_a[i], copy_a[j] = copy_a[j], copy_a[i]
            if copy_a == b:
                return True
            else:
                continue
    return False


print(areSimilar([1, 2, 3], [3, 1, 2]))
