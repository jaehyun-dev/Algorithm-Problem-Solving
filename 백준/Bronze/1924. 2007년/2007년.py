d = [0, 0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30]
for i in range(3, 13):
    d[i] = d[i - 1] + d[i]
x, y = map(int, input().split())
a = d[x] + y
print(["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"][a % 7])