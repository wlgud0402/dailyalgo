def solution(a, b):
    answer = 0
    zipped = list(zip(a, b))
    for i in range(len(zipped)):
        one_zip_mul = zipped[i][0] * zipped[i][1]
        answer += one_zip_mul
    return answer


def solution2(a, b):
    c = []
    for i in range(len(a)):
        c.append(a[i]*b[i])
    return sum(c)


print(solution([1, 2, 3, 4]	, [-3, -1, 0, 2]))  # 3
