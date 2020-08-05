# import copy

# def solution(strings):
#     answers = [strings[0]]
#     for i in range(1, len(strings)):
#         answers.append(strings[i])
#         new_answer = copy.deepcopy(answers)
#         for j in range(len(answers)):
#             try:
#                 if new_answer[j] == new_answer[j+1]:
#                     new_answer.pop(j+1)
#                     new_answer.pop(j)

#                     answers = new_answer
#             except:
#                 "에러요"

#     if len(answers) == 0:
#         return 1
#     else:
#         return 0

##############################22222222222222
# def solution(strings):
#     answers = [strings[0]]
#     for i in range(1, len(strings)):
#         answers.append(strings[i])
#         for j in range(len(answers)):
#             try:
#                 if answers[j] == answers[j+1]:
#                     answers.pop(j+1)
#                     answers.pop(j)
#             except:
#                 continue

#     if len(answers) == 0:
#         return 1
#     else:
#         return 0

#######################33333333333333333333
def solution(strings):
    answers = [strings[0]]
    for i in range(1, len(strings)):
        answers.append(strings[i])
        try:
            if answers[i-1] == answers[i]:
                answers.pop(i)
                answers.pop(i-1)
        except:
            continue

    if len(answers) == 0:
        return 1
    else:
        return 0


print(solution("baabaa")) #1
print(solution("cdcd")) #0