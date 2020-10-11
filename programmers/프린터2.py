import copy


def solution(priorities, location):
    priorities = [(i, v) for i, v in enumerate(priorities)]
    sorted_priorities = copy.deepcopy(priorities)

    for i in range(len(priorities)):
        for j in range(i, len(priorities)-1):
            if priorities[i][1] < priorities[j][1]:
                sorted_priorities.append(priorities[i])
                break

    cutting = len(sorted_priorities) - len(priorities)
    sorted_priorities = sorted_priorities[cutting:]

    for i in range(len(sorted_priorities)):
        if sorted_priorities[i][0] == location:
            return i+1

    print(sorted_priorities)


print(solution([2, 1, 3, 2]	, 2))
# 결과 return 1
