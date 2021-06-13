import sys
sys.stdin = open('txt/11656_접미사배열.txt')
own_strings = sys.stdin.readline()

part_strings = []
for i in range(len(own_strings)):
    part_strings.append(own_strings[i:])

part_strings.sort()

for string in part_strings:
    print(string)
