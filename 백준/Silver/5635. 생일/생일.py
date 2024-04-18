n = int(input())
a = []
for _ in range(n):
    name, day, month, year = list(input().split())
    a.append((year + month.zfill(2) + day, name))
a.sort()
print(a[-1][1])
print(a[0][1])