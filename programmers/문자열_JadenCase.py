def solution(string):
    string = string.split(' ')
    for i in range(len(string)):
        string[i] = string[i].capitalize()
    
    string = ' '.join(string)
    return string


print(solution("3people unFollowed me"))

#파이써닉한 방법 => title
def solution2(string):
    return string.title()

print(solution2("3people unFollowed me"))