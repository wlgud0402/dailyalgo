import sys
sys.stdin = open('txt/9012_괄호.txt')
string_count = int(sys.stdin.readline())

all_vars = []
for i in range(string_count):
    one_vars = sys.stdin.readline().replace("\n", "")
    all_vars.append(one_vars)

answers = []
for one_vars in all_vars:
    stack = []
    for var in one_vars:
        if not stack:
            stack.append(var)

        #구분 ( vs )
        else:
            if var == "(":
                stack.append(var)
            else:
                top = stack.pop()
                if top != var:
                    continue
                else:
                    stack.append(top)
                    stack.append(var)

    if stack:
        answers.append("NO")
    else:
        answers.append("YES")

for answer in answers:
    print(answer)
