a = list(map(int, input().split()))
a.sort()
b, c = a[0], a[2]
print(b * c)