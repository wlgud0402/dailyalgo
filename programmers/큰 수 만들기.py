def solution(number, k):
    number = [int(i) for i in number]
    for i in range(k + 1):
        flag = True
        for j in range(len(number)-1):
            if k == 0:
                return ''.join([str(i) for i in number])

            if number[j] < number[j+1]:
                number.pop(j)
                k -= 1
                flag = False
                break

        if flag:
            number.remove(min(number))
            k -= 1


print(solution("4177252841", 4))  # "775841"
# print()
print(solution("77766", 2))  # 94
