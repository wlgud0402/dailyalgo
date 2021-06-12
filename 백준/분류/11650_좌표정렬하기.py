import sys
sys.stdin = open('txt/11650_좌표정렬하기.txt')
line_count = int(sys.stdin.readline())


points = []
for i in range(line_count):
    x, y = map(int, sys.stdin.readline().split(" "))
    points.append([x, y])


sorted_points = sorted(points, key=lambda x: (x[0], x[1]))
for point in sorted_points:
    print(point[0], point[1])
