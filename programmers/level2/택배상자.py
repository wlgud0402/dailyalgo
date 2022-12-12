def solution(orders):
    prepare_stack = []
    answer = []
    for i in range(1, len(orders)+1):
        if i < orders[i-1]:
            prepare_stack.append(i)
        else:
            answer.append(i)
