import itertools
#zip을 통해서 한번 해보기

def solution(user_id, banned_ids):

    banned_list = []

    
    # for i in range(len(user_id)):
    #     for j in range(len(banned_ids)):
    #         if  
    # return answer
    union = list(itertools.product(user_id, banned_ids))

    for i in range(len(union)):
        flag = True
        print("밖에꺼 포문", flag)
        # print(union[i])
        for x, y in zip (union[i][0], union[i][1]):
            if x == y:
                print("x==y", x, y)
                continue

            if y == "*":
                print("*****", x, y)
                continue

            else:
                print("else",x, y)
                flag = False
                break
        print("안에꺼 포문", flag)
        
        # if flag:
        #     banned_list.append(union)

    print(banned_list)
        
    # for part in union:
    #     for i in range(len(part))







print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],["fr*d*" , "abc1**"]))

#출력 2
