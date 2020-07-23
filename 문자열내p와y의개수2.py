def solution(s):
    s = s.upper()
    if s.count("P") == s.count("Y"):
        return True
    else:
        return False


#lower나 upper를 사용한후 바로 count 사용가능
# == 연산자를 사용해서 같으면 True 다르면 False 의 boolean 값을 도출한다
def numPY(s):
    return s.lower().count('p') == s.lower().count('y')


print(solution("pPoooyY"))