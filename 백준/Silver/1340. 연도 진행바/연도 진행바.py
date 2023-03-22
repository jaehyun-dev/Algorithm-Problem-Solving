import datetime
import time
a = input().split()
month = {
    'January': 1,
    'February': 2,
    'March': 3,
    'April': 4,
    'May': 5,
    'June': 6,
    'July': 7,
    'August': 8,
    'September': 9,
    'October': 10,
    'November': 11,
    'December': 12
}
Month = month[a[0]]
DD = int(a[1][:2])
YYYY = int(a[2])
HH = int(a[3][:2])
MM = int(a[3][3:])
d = datetime.datetime(YYYY, Month, DD, HH, MM)
f = datetime.datetime(YYYY, 1, 1)
n = datetime.datetime(YYYY + 1, 1, 1)
print((d - f).total_seconds() / (n - f).total_seconds() * 100)