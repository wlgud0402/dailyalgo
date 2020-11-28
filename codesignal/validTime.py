def validTime(time):
    time = time.split(":")
    return 0 <= int(time[0]) < 24 and 0 <= int(time[1]) < 60


print(validTime("24:00"))
