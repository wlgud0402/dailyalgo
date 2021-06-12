import sys
sys.stdin = open('txt/2751_수정렬하기2.txt')
num_count = int(sys.stdin.readline())

numbers = []
for i in range(num_count):
    num = int(sys.stdin.readline())
    numbers.append(num)

numbers.sort()
for num in numbers:
    print(num)
