a = input()
year = int(a[:4]) - 1
month = int(a[5:7]) - 1
day = int(a[8:]) - 1
N = int(input())
d = year * 360 + month * 30 + day + N
year = d // 360
d %= 360
month = d // 30
d %= 30
day = d + 1
if 30 < day:
    day -= 30
    month += 1
if 12 < month:
    month -= 12
    year += 1
print(f"{year + 1}-{str(month + 1).zfill(2)}-{str(day).zfill(2)}")