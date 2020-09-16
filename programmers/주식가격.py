def solution(prices):
    answer = []
    sec = 0
    for i in range(0, len(prices)):
        for j in range(i+1, len(prices)):
            if prices[i] <= prices[j]:
                sec += 1
                continue
            else:
                sec+=1
                break
        answer.append(sec)
        sec = 0
    return answer
            # if 
            # if prices[i] <= prices[j]:
            #     print(prices[i], prices[j])
            #     sec +=1
            #     print("sec:  " ,sec)
            # elif prices[i] > prices[j]:
            #     answer.append(sec)
            #     print("answer: " ,answer)
            #     sec = 0
            # elif i == len(prices)-1:
            #     answer.append(0)
            #     break
    #         print(i, j)
    # return "결과"

prices = [1,2,3,2,3]

print(solution(prices))
