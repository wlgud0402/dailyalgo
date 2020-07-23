import datetime

class Solution:
    def dayOfTheWeek(self, day, month, year):
        daylist = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday","Sunday"]
        return daylist[datetime.date(year,month,day).weekday()]




solution = Solution()
print(solution.dayOfTheWeek(31,8,2019))
