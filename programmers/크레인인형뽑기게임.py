def solution(boards, moves):
    answer = 0
    bag =[]
    for move in moves:
        for row in boards:
            if row[move-1] != 0:
                bag.append(row[move-1])
                row[move-1] = 0
                break
        
        if len(bag) >= 2:
            if bag[len(bag)-1] == bag[len(bag)-2]:
                bag.pop()
                bag.pop()
                answer+=2
        
    return answer

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]],[1,5,3,5,1,2,1,4]))