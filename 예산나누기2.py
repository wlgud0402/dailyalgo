def solution(compayns, budget):
    compayns.sort()

    count = 0
    for i in range(len(compayns)):
        if budget >= compayns[i]:
            budget -= compayns[i]
            count +=1
    return count








print(solution([1,3,2,5,4],9))
print(solution([2,2,3,3],10))