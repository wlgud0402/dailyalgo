def solution(strings):
    strings = list(strings)
    # 모든 글자를 소문자로
    for i in range(len(strings)):
        strings[i] = strings[i].lower()

    # 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외하고 모두 제거
    for i in range(len(strings)):
        pass


print(solution("...!@BaT#*..y.abcdefghijklm"))
