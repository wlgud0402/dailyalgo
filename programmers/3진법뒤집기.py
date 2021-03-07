import string

tmp = string.digits+string.ascii_lowercase


def convert(num, base):
    q, r = divmod(num, base)
    if q == 0:
        return tmp[r]
    else:
        return convert(q, base) + tmp[r]


def solution(n):
    tmp = string.digits+string.ascii_lowercase
    q, r = divmod(n, 3)
    if q == 0:
        n = tmp[r]
    else:
        n = convert(q, 3) + tmp[r]

    n = n[::-1]
    answer = int(n, 3)
    return answer


print(solution(45))  # 45 => 1200 => 0021 => 7
