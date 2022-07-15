import sys
# push X: 정수 X를 스택에 넣는 연산이다.
# pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 스택에 들어있는 정수의 개수를 출력한다.
# empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
# top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.

sys.stdin = open('10828.txt')

order_count = int(sys.stdin.readline())
stack = []
for _ in range(order_count):
    order = sys.stdin.readline().split()
    if len(order) > 1:
        stack.append(int(order[1]))
        continue

    if order[-1] == "size":
        print(len(stack))
        continue

    if order[-1] == "top":
        if stack:
            print(stack[-1])
            continue
        else:
            print(-1)
            continue

    if order[-1] == "pop":
        if stack:
            top = stack.pop()
            print(top)
            continue
        else:
            print(-1)
            continue

    if order[-1] == "empty":
        if stack:
            print(0)
            continue
        else:
            print(1)
            continue
