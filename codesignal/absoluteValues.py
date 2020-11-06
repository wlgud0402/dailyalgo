def absoluteValuesSumMinimization(a):
    answer = []
    for num in a:
        one_sum = sum([abs(a[i] - num) for i in range(len(a))])
        answer.append(one_sum)
    min_idx = answer.index(min(answer))
    return a[min_idx]


print(absoluteValuesSumMinimization([2, 4, 7]))
