import copy


def solution(priorities, location):
    priorities_with_index = [(i, v) for i, v in enumerate(priorities)]
    copied = copy.deepcopy(priorities_with_index)
    for i in range(len(priorities)):
        for j in range(i+1, len(priorities)):
            if priorities[i] < priorities[j]:
                priorities_with_index.append(copied[i])
                priorities_with_index.pop(0)
                break

    for i, v in enumerate(priorities_with_index):
        if v[0] == location:
            return i+1


print(solution([1, 1, 9, 1, 1, 1], 0))
# location => index값 2 몇번째로 프린터되나? => 1번째(첫번째)
