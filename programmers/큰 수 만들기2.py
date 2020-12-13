import queue


def solution(number, k):
    number = [int(i) for i in number]
    stack = queue.deque()
    print(stack)
    stack = [number[0]]
    for i in range(k):
        for j in range(1, len(number)):
            if number[j] > stack[-1]:
                k -= 1
                stack.pop()
                stack.append(number[j])
                break
            else:
                stack.append(number[j])


print(solution("4177252841", 4))  # "775841"
# print()
print(solution("77766", 2))  # 94
