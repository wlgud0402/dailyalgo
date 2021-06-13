import sys
sys.stdin = open('txt/10828_스택.txt')
commands_count = int(sys.stdin.readline())

stack = []
for i in range(commands_count):
    command = sys.stdin.readline().split()
    if command[0] == "push":
        stack.append(command[1])

    if command[0] == "top":
        if stack:
            print(stack[-1])
        else:
            print(-1)

    if command[0] == "pop":
        if stack:
            top = stack.pop()
            print(top)
        else:
            print(-1)

    if command[0] == "size":
        print(len(stack))

    if command[0] == "empty":
        if stack:
            print(0)
        else:
            print(1)
