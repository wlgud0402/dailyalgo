import copy


def solution(priorities, location):
    priorities_with_index = [(i, v) for i, v in enumerate(priorities)]
    print(priorities_with_index)
    for i in range(len(priorities)):
        for j in range(i+1, len(priorities)):
            if priorities[i] < priorities[j]:
                print(priorities_with_index[i][1], priorities_with_index[j][1])
                priorities_with_index.append(priorities_with_index[i])
                priorities_with_index.pop(0)
                print(priorities_with_index)
                break
    return priorities_with_index


print(solution([2, 1, 3, 2], 2))
# location => index값 2 몇번째로 프린터되나? => 1번째(첫번째)
