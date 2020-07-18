from datetime import datetime, timedelta

class Solution:
    def daysBetweenDates(self, date1, date2):
        date1 = datetime.strptime(date1,'%Y-%m-%d')
        date2 = datetime.strptime(date2,'%Y-%m-%d')
        
        diff = (date1-date2).days
        return abs(diff)



solution = Solution()
print(solution.daysBetweenDates("2019-06-29","2019-06-30"))
print(solution.daysBetweenDates("2020-01-15","2019-12-31"))

# from datetime import datetime, timedelta

# class Solution:
#     def daysBetweenDates2(self, date1, date2):
#         date1 = datetime.strptime(date1,'%Y-%m-%d')
#         date2 = datetime.strptime(date2,'%Y-%m-%d')
        
#         diff = str(date1-date2)
#         diff = diff.split(" ")
#         diff = diff[0]
#         diff = int(diff)
#         return abs(diff)

# solution = Solution()
# print(solution.daysBetweenDates2("2019-06-29","2019-06-30"))
# print(solution.daysBetweenDates2("2020-01-15","2019-12-31"))