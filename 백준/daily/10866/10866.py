
import sys
from collections import deque

sys.stdin = open('10866.txt')

order_count = int(sys.stdin.readline())
queue = deque()
for _ in range(order_count):
    order = sys.stdin.readline().strip().split()
    if order[0] == "empty":
        if not queue:
            print(1)
            continue
        else:
            print(0)
            continue

    if order[0] == "push_back":
        queue.append(int(order[1]))
        continue

    if order[0] == "push_front":
        queue.appendleft(int(order[1]))
        continue

    if order[0] == "pop_front":
        if queue:
            front = queue.popleft()
            print(front)
            continue
        else:
            print(-1)
            continue

    if order[0] == "pop_back":
        if queue:
            back = queue.pop()
            print(back)
            continue
        else:
            print(-1)
            continue

    if order[0] == "size":
        print(len(queue))
        continue

    if order[0] == "front":
        if queue:
            print(queue[0])
            continue
        else:
            print(-1)
            continue

    if order[0] == "back":
        if queue:
            print(queue[-1])
            continue
        else:
            print(-1)
            continue
