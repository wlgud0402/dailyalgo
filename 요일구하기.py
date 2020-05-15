import calendar

def solution(month, day):
    days=["MON","TUE","WED","THU","FRI","SAT","SUN"]
    date = calendar.weekday(2016, month, day)
    return days[date]

print(solution(5,24))

