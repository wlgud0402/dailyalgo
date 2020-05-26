def solution(bridge_length, handle_weight, truck_wating):
    sec = 0 
    passing = []
    done_sec = []
    passing.append(truck_wating[0])
    for i in range(1, len(truck_wating)):
        if handle_weight >= passing[-1] + truck_wating[i]:
            passing.append(truck_wating[i])
            sec +=1
            print("1번째:", sec,passing,done_sec,truck_wating[i])
            continue
        elif bridge_length == sec:
            done_sec.append(sec)
            passing.pop(0)
            sec = 0
            print("2번째:", sec,passing,done_sec,truck_wating[i])
            continue
        elif handle_weight < passing[-1] + truck_wating[i]:
            # passing.append(truck_wating[i])
            sec +=1
            print("3번째:", sec,passing,done_sec,truck_wating[i])
            continue
    sum(done_sec)
    # print(sec,passing,done_sec)
    return done_sec 


print(solution(2, 10, [7,4,5,6]))