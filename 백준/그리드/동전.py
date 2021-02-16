import sys
sys.stdin = open('동전.txt')
N, K = map(int, sys.stdin.readline().split(" "))

worths = []
for i in range(N):
    worth = int(sys.stdin.readline())
    worths.append(worth)

coin_count = 0
while K != 0:
    for i in range(N-1, -1, -1):
        if worths[i] <= K:
            K -= worths[i]
            coin_count += 1
            break
print(coin_count)
