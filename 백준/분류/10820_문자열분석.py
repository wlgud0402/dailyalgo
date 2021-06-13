import sys
sys.stdin = open('txt/10820_문자열분석.txt')
# 소문자, 대문자, 숫자, 공백

while True:
    strings = list(map(str, sys.stdin.readline()))
    if not strings:
        break

    lower = 0
    upper = 0
    digit = 0
    space = 0

    for string in strings:
        if string.islower():
            lower += 1

        if string.isupper():
            upper += 1

        if string.isdigit():
            digit += 1

        if string == " ":
            space += 1

    print(lower, upper, digit, space)
