s = 0
n = 0
for i in range(1, 6):
    a = sum(list(map(int, input().split())))
    if a > s:
        s = a
        n = i
print(n, s)