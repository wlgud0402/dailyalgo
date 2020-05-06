#장난스럽게 하긴 했지만 쓰레기같은 방법
def solution(phone_number):
    answer=[]
    for i in range(len(phone_number)-4):
        answer+="*"
    answer+=phone_number[-4:]
    answer = "".join(answer)
    return answer

print(solution("01068051234"))


#반복문, 새로운 리스트, 다시 문자열로의 변환이 없는 깔끔한 방법
def hide_numbers(s):
    return "*"*(len(s)-4) + s[-4:]


print("결과 : " + hide_numbers('01033334444'))