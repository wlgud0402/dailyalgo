def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        start = commands[i][0]
        end = commands[i][1]
        idx = commands[i][2]

        after = array[start-1:end]
        after.sort()
        answer.append(after[idx-1])

    return answer




print(solution([1, 5, 2, 6, 3, 7, 4],[[2, 5, 3], [4, 4, 1], [1, 7, 3]]))