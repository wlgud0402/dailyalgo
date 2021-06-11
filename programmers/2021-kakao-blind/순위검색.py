def compare(condition, user_condition):
    flag = False
    if (condition[0] == "-" or condition[0] == user_condition[0]) and \
        (condition[1] == "-" or condition[1] == user_condition[1]) and\
        (condition[2] == "-" or condition[2] == user_condition[2]) and\
        (condition[3] == "-" or condition[3] == user_condition[3]) and \
            (int(condition[4]) <= int(user_condition[4])):
        flag = True

    return flag


def solution(infos, querys):
    answers = []
    for query in querys:
        count = 0
        condition = query.replace("and", " ").split()

        for info in infos:
            user_condition = info.replace("and", " ").split()
            flag = compare(condition, user_condition)
            if flag:
                count += 1
        answers.append(count)
    return answers


print(solution(["java backend junior pizza 150",
                "python frontend senior chicken 210",
                "python frontend senior chicken 150",
                "cpp backend senior pizza 260",
                "java backend junior chicken 80",
                "python backend senior chicken 50"],

               ["java and backend and junior and pizza 100",
                "python and frontend and senior and chicken 200",
                "cpp and - and senior and pizza 250",
                "- and backend and senior and - 150",
                "- and - and - and chicken 100",
                "- and - and - and - 150"]))

# [1,1,1,1,2,4]
