def solution(sentence):
    idx = 0
    answer = ''
    for letter in sentence:
        if letter == ' ':
            idx = 0
        else:
            if idx % 2 == 0:
                letter = letter.upper()
            else:
                letter = letter.lower()
            idx +=1
        answer += letter
    return answer

print(solution("try hello        world"))

def solution2(sentence):
    sentence =sentence.split(" ") #띄어쓰기를 넣고 split으로 나누면 공백또한 하나의 요소로 취급하면서 단어로 분할시켜줌
    return sentence

print(solution2("try hello       world"))

