import sys
sys.stdin = open('거스름돈.txt')
M = int(sys.stdin.readline())

changes = [500, 100, 50, 10, 5, 1]

change = 1000 - M
c_count = 0

while change != 0:
    for c in changes:
        if change >= c:
            change -= c
            c_count += 1
            break

print(c_count)
