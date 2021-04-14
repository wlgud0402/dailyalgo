import sys
from collections import deque

sys.stdin = open('스택.txt')
order_count = int(input())
orders = []
for i in range(order_count):
    order = input()
    orders.append(order)

stack = []
for i in range(len(orders)):
    one_order = orders[i].split(" ")
    if one_order[0] == "push":
        stack.append(int(one_order[1]))

    if one_order[0] == "pop":
        if len(stack) == 0:
            print(-1)
        else:
            popped = stack.pop()
            print(popped)

    if one_order[0] == "top":
        if len(stack) != 0:
            print(stack[-1])
        else:
            print(-1)

    if one_order[0] == "size":
        print(len(stack))

    if one_order[0] == "empty":
        if len(stack) == 0:
            print(1)
        else:
            print(0)
