def solution(companys, budget):
    companys.sort()
    answer =0
    for i in range(len(companys)):
        if budget < companys[i]:
            break
        else:
            budget -= companys[i]
            answer +=1

    return answer
    
print(solution(	[2, 2, 3, 3], 10))

#sort로 숫자들을 한번 정렬해서 논리적용하기 쉽게