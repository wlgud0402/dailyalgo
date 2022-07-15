import sys
sys.stdin = open('9012.txt')

line_count = int(sys.stdin.readline())
for _ in range(line_count):
    strings = sys.stdin.readline().strip()
    stack = []
    for string in strings:
        if not stack:
            stack.append(string)
            continue

        top = stack.pop()
        if top == "(" and string == ")":
            continue
        else:
            stack.append(top)
            stack.append(string)
    if stack:
        print("NO")
    else:
        print("YES")
