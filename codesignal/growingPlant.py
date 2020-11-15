def growingPlant(upSpeed, downSpeed, desiredHeight):
    now_height = 0
    day_count = 0
    while now_height < desiredHeight:
        day_count += 1

        now_height += upSpeed
        if now_height >= desiredHeight:
            return day_count

        now_height -= downSpeed
        if now_height >= desiredHeight:
            return day_count

# def growingPlant(upSpeed, downSpeed, desiredHeight):
#     height = 0
#     days = 1
#     height += upSpeed
#     while height < desiredHeight:
#         days += 1
#         height -= downSpeed
#         height += upSpeed
#     return days


# print(growingPlant(100, 10, 910))  # 10
print(growingPlant(5, 2, 7))  # 2
