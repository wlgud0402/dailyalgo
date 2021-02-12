from copy import deepcopy


def solution(priorities, location):
    copy_priorities = deepcopy(priorities)
    # flag = True
    value_idx = [(v, i) for i, v in enumerate(priorities)]
    print(value_idx)

    while True:
        flag = True
        for i in range(len(value_idx)):
            for j in range(i+1, len(value_idx)):
                if value_idx[i][0] < value_idx[j][0] and flag:
                    value_idx.pop(i)
                    value_idx.append(value_idx[i])
                    flag = False
                    break
        print(value_idx)


print(solution([2, 1, 3, 2]	, 2))
# 결과 return 1
