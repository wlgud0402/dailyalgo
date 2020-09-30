# def solution(n):
#     numbers = [i+1 for i in range(1, n)]
#     answers = []
#     for n in numbers:
#         count = 0
#         flag = True
#         for i in range(1, n+1):
#             if n % i == 0:
#                 count += 1
#             if count > 2:
#                 flag = False
#                 break
#         if flag:
#             answers.append(n)
#     return len(answers)
def solution(n):
    answers = []
    for i in range(2, n+1):
        count = 1
        flag = True
        for j in range(1, i+1):
            if count > 2:
                flag = False

            if i % j == 0:
                count += 1

        if flag:
            answers.append(n)
    return len(answers)


print(solution(5))
# 2,3,5,7
