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

# def solution(n, lost, reserve):
#     if len(lost) == 0:
#         return n

#     for i in reserve:
#         for j in lost:
#             if i == j:
#                 lost.remove(i)
#                 reserve.remove(j)
#             elif i-1 == j:
#                 lost.remove(j)
#             elif i+1 == j:
#                 lost.remove(j)
#     return n - len(lost)

# print(solution(5,[2,3,4],[1,3,5]))

# def solution(n, lost, reserve):
#     if len(lost) == 0:
#         return n

#     for j in lost:
#         for i in reserve:
#             if i == j:
#                 lost.remove(j)
#                 reserve.remove(i)
#             elif i-1 == j:
#                 lost.remove(j)
#                 reserve.remove(i)
#             elif i+1 == j:
#                 lost.remove(j)
#                 reserve.remove(i)
#     return n - len(lost)

# def burrow(n, lost, reserve):
#     in

# b1 = set([1,2,3,4,5])
# b2 = set([3,5])

# b3= b1.intersection(b2)

# b4 = b1.difference(b3)

# print(b4)

def solution(n, lost, reserve):
    lost = set(lost)
    reserve = set(reserve)
    common = lost.intersection(reserve)

    lost = list(lost.difference(common))
    find = set()
    reserve = list(reserve.difference(common))

    for lost_stu in lost:
        front_stu = lost_stu - 1
        back_stu = lost_stu + 1
        if front_stu in reserve:
            # lost.remove(lost_stu)
            find.add(lost_stu)
            reserve.remove(front_stu)                
            continue
        if back_stu in reserve:
            # lost.remove(lost_stu)
            find.add(lost_stu)
            reserve.remove(back_stu)
            continue
        

    return n - len(lost) + len(find)

def solution2(n, lost, reserve):
    lost = set(lost)
    reserve = set(reserve)
    find = set()

    for lost_stu in lost:
        front_stu = lost_stu - 1
        back_stu = lost_stu + 1
        if lost_stu in reserve:
            find.add(lost_stu)
            reserve.remove(lost_stu)                
            continue
        if front_stu in reserve:
            # lost.remove(lost_stu)
            find.add(lost_stu)
            reserve.remove(front_stu)                
            continue
        if back_stu in reserve:
            # lost.remove(lost_stu)
            find.add(lost_stu)
            reserve.remove(back_stu)
            continue
        

    return n - len(lost) + len(find)

print(solution2(5, [2, 4], [1, 3, 5])) #5
print(solution2(5, [2, 4], [3])) #4
print(solution2(3, [3], [1])) #2
print(solution2(5, [2,3], [2,3]))
