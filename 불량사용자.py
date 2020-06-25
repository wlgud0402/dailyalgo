import itertools
#zip을 통해서 한번 해보기

from functools import reduce

def solution(user_id, banned_ids):

    banned_list = []
    table = {}
    union = list(itertools.product(user_id, banned_ids))
    same_id_table = {}

    
    for i in range(len(union)):
        flag = True
        #print("밖에꺼 포문", flag)
        # print(union[i])
        for x, y in zip (union[i][0], union[i][1]):

            if len(union[i][0]) != len(union[i][1]):
                flag = False
                break

            if x == y:
                #print("x==y", x, y)
                continue

            if y == "*":
                #print("*****", x, y)
                continue

            else:
                #print("else",x, y)
                flag = False
                break
        #print("안에꺼 포문", flag)
        
        if flag:
            banned_list.append(union[i])
    
    #print("처음",banned_list)

    banned_list = list(set(banned_list))

    print("중복제거후",banned_list)

    pass

    for banned in banned_list:
        if banned[1] in table:
            print("banned1",banned[1])
            #table[banned[1]] += 1
            table[banned[1]] += banned[0]
            table[banned[1]] += " "
            print("인쇄",table[banned[1]] )
        else:
            print("elsebanned1",banned[1])
            #table[banned[1]] = 1
            table[banned[1]] = banned[0] 
            table[banned[1]] += " "
    
    for banned in table:
        # table[banned[1]] = table[banned[1]].split()
        table[banned] = table[banned].split()

    print("table",table)

    values = []

    for value in table.values():
        values.append(len(value))

        # return reduce(lambda x, y: x*y, values)
    print(values)


    for banned_id in banned_ids:
        if banned_id in same_id_table:
            same_id_table[banned_id] += 1
        else:
            same_id_table[banned_id] = 1
    
    print("same테이브르르르를ㄹ",same_id_table)
    #겹치는 값의 곱 => 나중에 값곱집합의 곱셈에서 나눠줌

    values2 = []
    for value2 in same_id_table.values():
        values2.append(value2)
    print(values2)
    # return reduce(lambda x, y: x*y, values2)

    #values의 누적곱 / values2의 누적곱   - len(처음 겹치는banned_id)

    return values, values2


    
    


    # return reduce(lambda x, y: x*y, values)


# print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],["fr*d*" , "abc1**"]))
# print(solution(	["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"]))
print()
print()
print()
print()
print()



print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],	["fr*d*", "*rodo", "******", "******"]))


#출력 2
