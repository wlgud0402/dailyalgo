def solution(numbers):
    bundle = [(i, int(str(num)[:1])) for i, num in enumerate(numbers)]
    bundle.sort(key=lambda ele: ele[1])
    answer = ''
    for i in range(len(bundle)-1, -1, -1):
        num_index = bundle[i][0]
        answer += str(numbers[num_index])
    return answer


print(solution([6, 10, 2]))
# "6210"
