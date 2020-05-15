def solution1(tops):
    answer = []
    for i in range(len(tops)):
        appended = False
        for j in range(i - 1, 0 - 1, -1):
            if tops[j] > tops[i]:
                answer.append(j+1)
                appended = True
                break
        if not appended:
            answer.append(0)

    return answer
    #솔루션 1에서는 작은 포문을 돌았는데 만약 추가되지 않았다면 0 을 추가라는 로직을 => appended라는 플래그를 만들어서 해결함

def solution2(tops):
    answer = [0] * len(tops)
    for i in range(len(tops)):
        #print("i=",i)
        for j in range(i - 1, 0 - 1, -1):
            #print(tops[j], tops[i])
            if tops[j] > tops[i]:
                answer[i] = j+1
                #print("if문속",tops[j],tops[i])
                break

    return answer
    #솔루션1과 솔루션2 둘다 마찬가지로 자신보다 작은걸 비교할때 for문에서 위에는 i로 돌리고 아래는 i-1로 돌리면 자신과 작은거까지만 딱 비교하게 된다.

print(solution1([6,9,5,7,4]))
print(solution2([6,9,5,7,4]))