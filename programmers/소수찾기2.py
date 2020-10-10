def solution(n):
    answers = []
    for i in range(2, n):
        count = 0
        for j in range(1, i):
            print(i, j)
            if i % j == 0:
                count += 1
        if count == 1:
            print("i", i)
            answers.append(i)

    return len(answers), answers


print(solution(5))
# 2,3,5,7
