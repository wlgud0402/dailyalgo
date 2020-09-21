# import copy


# def solution(peoples, limit):
#     peoples.sort()
#     count = 0
#     while peoples:
#         flag = True
#         boat_limit = copy.deepcopy(limit)
#         for _ in range(len(peoples)):
#             if peoples[0] <= boat_limit and flag == True:
#                 count += 1
#                 boat_limit -= peoples[0]
#                 peoples.pop(0)
#                 flag = False
#             elif peoples[0] <= boat_limit and flag == False:
#                 peoples.pop(0)
#                 continue
#     return count


print(solution([70, 50, 80, 50], 100))
