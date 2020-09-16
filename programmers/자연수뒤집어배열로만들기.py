def solution(number):
    number_list = [int(n) for n in str(number)]
    number_list.reverse()
    return number_list

print(solution(12345))

def digit_reverse(n):
    return list(map(int, reversed(str(n))))
#아예 처음부터 숫자를 문자화> 뒤집기 >> 다시 숫자로 map핑 >> 그리고 리스트화