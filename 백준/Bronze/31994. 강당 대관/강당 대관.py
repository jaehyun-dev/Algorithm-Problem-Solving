l = []
for _ in range(7):
    a = input().split()
    l.append((int(a[1]), a[0]))
l.sort(reverse=True)
print(l[0][1])