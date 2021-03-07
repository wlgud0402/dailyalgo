def solution(N, stages):
    stages.sort()
    failure = []
    for i in range(1, N+1):
        trying_count = 0
        success_count = 0
        for s in stages:
            if i == s:
                trying_count += 1
            if i < s:
                success_count += 1

        if trying_count == 0 and success_count == 0:
            failure.append([i, 0])
        else:
            failure.append([i,
                            trying_count/(trying_count+success_count)])
    sorted_by_fail_stage = sorted(
        failure, key=lambda x: (x[1], -x[0]), reverse=True)

    # print(sorted_by_fail_stage)

    answer = [s[0] for s in sorted_by_fail_stage]
    return answer


print(solution(5, 	[2, 1, 2, 6, 2, 4, 3, 3]))
# [3,4,2,1,5]
