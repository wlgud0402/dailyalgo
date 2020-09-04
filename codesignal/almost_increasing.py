def almostIncreasingSequence(sequence):
    flag = 0
    for i in range(len(sequence)-1):
        if sequence[i] < sequence[i+1]:
            continue
        else:
            flag += 1
            if flag >= 2:
                return False
            else:
                continue
    return True

print(almostIncreasingSequence([1,2,1,2]))