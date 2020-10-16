# -*- coding: utf-8 -*-
def areSimilar(a, b):
    if a == b:
        return True

    a = set([(i, v) for i, v in enumerate(a)])
    b = set([(i, v) for i, v in enumerate(b)])

    only_a = list(a-b)
    only_b = list(b-a)

    ordered_a = sorted(only_a, key=lambda x: x[0])
    ordered_b = sorted(only_b, key=lambda x: x[0])

    if len(only_a) == 2 and len(only_b) == 2:
        if ordered_a[0][1] == ordered_b[1][1] and ordered_a[1][1] == ordered_b[0][1]:
            return True
        else:
            return False
    else:
        return False


print(areSimilar([1, 2, 3], [2, 1, 3]))
# 123 124
