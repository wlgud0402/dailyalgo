from collections import deque
from copy import deepcopy

def solution(numbers, target):
    queue =deque()
    queue.append([numbers[0]])
    queue.append([-numbers[0]])
    
    count = 0
    while len(queue) > 0:
        curr_path = queue.popleft()
        if len(curr_path) == len(numbers) and sum(curr_path) == target:
            count += 1
            continue

        try:
            target_index = len(curr_path)
            curr_target = numbers[target_index]

            curr_plus_path = curr_path[:]
            curr_minus_path = curr_path[:]

            curr_plus_path.append(curr_target)
            curr_minus_path.append(-curr_target)

            queue.append(curr_plus_path)
            queue.append(curr_minus_path)
            continue

        except:
            continue

    return count

from itertools import product
def solution2(numbers, target):
    l = [(x, -x) for x in numbers]
    s = list(map(sum, product(*l)))
    return s.count(target)



print(solution([1, 1, 1, 1, 1],3))#5