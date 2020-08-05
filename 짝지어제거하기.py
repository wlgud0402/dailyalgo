import copy

def solution(strings):
    answers = [strings[0]]
    for i in range(1, len(strings)):
        answers.append(strings[i])
        new_answer = copy.deepcopy(answers)
        for j in range(len(answers)):
            try:
                if new_answer[j] == new_answer[j+1]:
                    new_answer.pop(j+1)
                    new_answer.pop(j)

                    answers = new_answer
            except:
                "에러요"

    if len(answers) == 0:
        return 1
    else:
        return 0





print(solution("baabaa")) #1
print(solution("cdcd")) #0