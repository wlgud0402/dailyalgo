#체육복문제
def solution(n, lost, reserve):
    students = [1 for i in range(n)]

    #잃어버린 사람꺼 -1
    for i in range(len(lost)):
        students[lost[i]-1] -= 1 

    #여분으로 가져온 사람 +1
    for i in range(len(reserve)):
        students[reserve[i]-1] += 1 

    # 1개 넘개 가지고 있는 사람은 전사람 줄수있는지 보고, 아니면 다음사람한테 줌
    for i in range(len(students)):
        try:
            if students[i] > 1 and students[i-1] == 0:
                students[i] -= 1
                students[i-1] += 1
                continue
            elif students[i] > 1 and students[i+1] == 0:
                students[i] -= 1
                students[i+1] += 1
                continue
            else:
                continue
        except:
            continue
    
    #1개 이상이기만 하면 수업 듣기 가능
    count = 0
    for i in range(len(students)):
        if students[i] >= 1:
            count +=1
            continue
    return count


print(solution(5, [2,4], [1,3,5]))