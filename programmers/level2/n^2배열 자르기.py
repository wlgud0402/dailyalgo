def solution(n, left, right):
    answer = []
    for point in range(left, right + 1):
        head = point // n
        remain = point % n
        answer.append(max(head, remain) + 1)
    return answer
