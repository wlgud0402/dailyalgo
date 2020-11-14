# time exceed
def almostIncreasingSequence(sequence):
    if len(sequence) - len(set(sequence)) > 1:
        return False

    if len(sequence) == 1:
        return True

    for i in range(len(sequence)):
        popped = sequence[:i] + sequence[i+1:]
        if sorted(popped) == popped:
            return True
        else:
            continue

    return False


print(almostIncreasingSequence([1, 2, 3, 4, 5, 4, 6]))
