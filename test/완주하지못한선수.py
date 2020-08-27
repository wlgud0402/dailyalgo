#for 문과in 연산을 통하기 때문에 시간초과일어남
# def solution(participant, completion):
#     for runner in participant:
#         if runner in completion:
#             completion.remove(runner)
#         else:
#             return runner
# print(solution(["leo", "kiki", "eden"],["eden", "kiki"]))

def solution2(participant, completion):
    count = {}
    for runner in completion:
        if runner not in count:
            count[runner] = 1
        else:
            count[runner] += 1

    for runner in participant:
        if runner in count and count[runner] >= 1:
            count[runner] -= 1
        else:
            return runner
    


print(solution2(["mislav", "stanko", "mislav", "ana"],["stanko", "ana", "mislav"]))