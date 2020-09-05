# def almostIncreasingSequence(sequence):
#     if len(sequence) - len(set(sequence)) > 1:
#         return False

#     flag = 0
#     for i in range(len(sequence)-1):
#         if sequence[i] < sequence[i+1]:
#             continue
#         else:
#             flag += 1
#             if flag >= 2:
#                 return False
#             else:
#                 continue
#     return True

def almostIncreasingSequence(sequence):
    if len(sequence) - len(set(sequence)) > 1:
        return False

    for i in range(len(sequence)):
        poped_sequence = list(sequence)
        poped_sequence.pop(i)
        if sorted(poped_sequence) == poped_sequence:
            return True
        continue
    return False


#         if sequence == sorted(list(set(sequence))): return True

print(almostIncreasingSequence([1, 2, 3, 4, 3, 6]))