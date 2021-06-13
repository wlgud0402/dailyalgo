from collections import deque
import sys
sys.stdin = open('txt/10866_덱.txt')
commands_count = int(sys.stdin.readline())

queue = deque()
for i in range(commands_count):
    command = sys.stdin.readline().split()
    if command[0] == "push_front":
        queue.appendleft(command[1])

    if command[0] == "push_back":
        queue.append(command[1])

    if command[0] == "pop_front":
        if queue:
            print(queue.popleft())
        else:
            print(-1)

    if command[0] == "pop_back":
        if queue:
            print(queue.pop())
        else:
            print(-1)

    if command[0] == "size":
        print(len(queue))

    if command[0] == "empty":
        if queue:
            print(0)
        else:
            print(1)

    if command[0] == "front":
        if queue:
            print(queue[0])
        else:
            print(-1)

    if command[0] == "back":
        if queue:
            print(queue[-1])
        else:
            print(-1)
