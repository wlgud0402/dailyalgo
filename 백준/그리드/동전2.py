import sys
sys.stdin = open('동전.txt')
N, K = map(int, sys.stdin.readline().split(" "))

worths = []
for i in range(N):
    worth = int(sys.stdin.readline())
    worths.append(worth)

coint_count = 0
for i in range(N-1, -1, -1):
    if K >= worths[i]:
        coint_count += K//worths[i]
        K = K % worths[i]
print(coint_count)
