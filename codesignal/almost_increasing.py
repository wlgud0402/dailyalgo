#time exceed
def almostIncreasingSequence(sequence):
    if len(sequence) - len(set(sequence)) > 1:
        return False
    
    if len(sequence) == 1:
        return True


    for i in range(len(sequence)):
        poped_sequence = list(sequence)
        poped_sequence.pop(i)
        if sorted(poped_sequence) == poped_sequence:
            return True
        continue
    return False


#if sequence == sorted(list(set(sequence))): return True

#right answer
def almostIncreasingSequence(sequence):
    sequence_len = len(sequence)
    p = -1
    count = 0

    for i in range(1,sequence_len):
        if sequence[i-1] >= sequence[i]:
            p = i
            count += 1
    
    if count > 1: return False

    if count == 0:
        return True #ok

    if p == sequence_len-1 or p == 1: 
        return True #p == sequence_len-1 (마지막 경우에서 제거하는 경우) #p == 1 (첫번째에서 제거하는 경우)

    if sequence[p-1] < sequence[p+1]: #p의 양쪽끼리 비교했을때 문제가 없을시 문제되는것은 p인덱스의 값
        return True

    if sequence[p-2] < sequence[p]:  #위의 경우를 지나쳐 온후 p-2 의 값과 p를 비교했을때 문제가 없다면 True
                                     #문제가 있다면 False
        return True
    else:
        return False

print(almostIncreasingSequence([1, 2, 3, 4, 5, 4, 6]))

print(almostIncreasingSequence([1, 2, 3, 4, 3, 6]))