import sys
sys.stdin = open('게임을만든동준이.txt')
level = int(sys.stdin.readline())

points = []
minus_point = 0

for i in range(level):
    point = int(sys.stdin.readline())
    points.append(point)


for i in range(level-1, 0, -1):
    if points[i-1] >= points[i]:
        minus_point += (points[i-1] - points[i] + 1)
        points[i-1] = points[i] - 1
print(minus_point)
