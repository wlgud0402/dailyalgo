#역순으로 정렬
def solution(number):
    before_sort = [n for n in str(number)]

    after_sort = sorted(before_sort, reverse=True)
    answer = ''.join(after_sort)

    return int(answer)

print(solution(118372))
#873211