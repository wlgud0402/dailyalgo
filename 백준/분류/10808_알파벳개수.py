import sys
sys.stdin = open('txt/10808_알파벳개수.txt')
strings = list(map(str, sys.stdin.readline()))

alphas = [0] * 26

for string in strings:
    idx = ord(string) - 97
    alphas[idx] += 1

for alpha in alphas:
    print(alpha, end=' ')
