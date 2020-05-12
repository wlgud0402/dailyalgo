# def solution(n, lost, reserve):
#     check =[]
#     check.append(lost[0])
#     for i in range(len(reverse)):
#         if reverse[i] -1 == check[0] or reverse[i] +1 == check[0]:

#     return answers

# def solution(n, lost, reserve):
#     for i in range(len(reserve)):
#         if reserve[i]+1 in lost:
#             lost.remove(reserve[i]+1)
#             reserve.pop(i)
#         elif reserve[i]-1 in lost:
#             lost.remove(reserve[i]-1)
#             reserve.pop(i)
#     return n - len(lost)

# print(solution(5,[2,4],[3]))

# def solution(n, lost, reserve):
#     for i in reserve:
#         if i+1 in lost:
#             lost.remove(i+1)
#         elif i-1 in lost:
#             lost.remove(i-1)
#     return n - len(lost)

# print(solution(5,[2,4],[1,3,5]))

def solution(n, lost, reserve):
    if len(lost) == 0:
        return n

    for i in reserve:
        for j in lost:
            if i == j:
                lost.remove(i)
                reserve.remove(j)
            elif i-1 == j:
                lost.remove(j)
            elif i+1 == j:
                lost.remove(j)
    return n - len(lost)

print(solution(5,[2,3,4],[1,3,5]))

def solution(n, lost, reserve):
    if len(lost) == 0:
        return n

    for j in lost:
        for i in reserve:
            if i == j:
                continue
            elif i-1 == j:
                lost.remove(j)
            elif i+1 == j:
                lost.remove(j)
    return n - len(lost)
