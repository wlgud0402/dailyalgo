def solution(people, limit):
    people.sort()

    count = 0
    while people:
        new_limit = limit
        flag = True
        for i in range(len(people)):
            if people[0] <= new_limit and flag == True:
                count +=1
                new_limit -= people[0]
                people.pop(0)
                flag = False
                continue

            elif flag == False and people[0] <= new_limit:
                new_limit -= people[0]
                people.pop(0)
                continue
            else:       
                break

    return count


print(solution([70, 50, 80, 50], 100))
#50,50,70,80