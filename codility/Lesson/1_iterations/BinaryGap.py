def solution(N):
    bin_num = bin(N)    
    zero_lengths = bin_num.split("1")[1:-1]
    if zero_lengths == []:
        return 0

    max_zero = max(zero_lengths)
    return len(max_zero)

#올바른 풀이
def solution2(N):
    return len(max(bin(N)[2:].strip('0').split('1'))) 



print(solution(328))
print(solution2(328))
