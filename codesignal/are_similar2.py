import copy


def areSimilar(a, b):
    copy_a = copy.deepcopy(a)
    copy_b = copy.deepcopy(b)

    for i in range(len(a)):
        if a[i] == b[i]:
            copy_a.remove(a[i])
            copy_b.remove(b[i])

    if copy_a[::-1] == copy_b:
        return True
    else:
        return False


print(areSimilar([1, 2, 3], [1, 3, 2]))
# 123 124
