def solution(x):
    nums = list(str(x))
    div = 0
    for num in nums:
        div += int(num)
    
    if x % div == 0:
        return True
    else:
        return False

print(solution(10))
# numbers = list(map(int, list(str(x))))
#한개의 숫자 x 를 문자열로 쪼갠후 리스트화 => 숫자화 => map으로 감싸여 있으므로 list로 꺼냄