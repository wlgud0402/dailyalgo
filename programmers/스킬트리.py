def solution(skill, skill_trees):
    answer = 0
    matches = []

    for skill_tree in skill_trees:
        append_s=""
        for s in skill_tree:
            if s in skill:
                append_s+=s
        matches.append(append_s)

    for match in matches:
        flag = True
        for i in range(len(match)):
            if match[i] == skill[i]:
                continue
            else:
                flag = False
                break
        if flag:
            answer += 1
    return answer

#['BCD', 'CBD', 'CB', 'BD']

print(solution("CBD" , ["BACDE", "CBADF", "AECB", "BDA"]))
#출력 => CBADF, AECB 2개