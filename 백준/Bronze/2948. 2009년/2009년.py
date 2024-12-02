import datetime
import calendar
D, M = map(int, input().split())
print(calendar.day_name[datetime.date(2009, M, D).weekday()])