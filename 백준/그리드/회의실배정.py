# confs = [[1, 4],
#          [3, 5],
#          [0, 6],
#          [5, 7],
#          [3, 8],
#          [5, 9],
#          [6, 10],
#          [8, 11],
#          [8, 12],
#          [2, 13],
#          [12, 14]]

# sorted_confs = sorted(confs, key=lambda x: (x[1], x[0]))
# end = 0
# count = 0
# for i in range(len(sorted_confs)):
#     if end <= sorted_confs[i][0]:
#         end = sorted_confs[i][1]
#         count += 1
# print(count)

import sys

sys.stdin = open('회의실배정.txt')
conf_count = int(input())
confs = []
for i in range(conf_count):
    start, end = map(int, input().split())
    confs.append([start, end])

sorted_confs = sorted(confs, key=lambda x: (x[1], x[0]))
end = 0
count = 0
for i in range(len(sorted_confs)):
    if end <= sorted_confs[i][0]:
        end = sorted_confs[i][1]
        count += 1
print(count)
