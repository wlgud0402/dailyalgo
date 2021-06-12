import sys
sys.stdin = open('txt/11650_좌표정렬하기2.txt')
line_count = int(sys.stdin.readline())


points = []
for i in range(line_count):
    x, y = map(int, sys.stdin.readline().split(" "))
    points.append([x, y])


sorted_points = sorted(points, key=lambda x: (x[1], x[0]))
for point in sorted_points:
    print(point[0], point[1])
