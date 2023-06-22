n, T = map(int, input().split())
a = list(map(int, input().split()))
count = 0
i = 0
while i < n:
    count += a[i]
    if count > T:
        break
    i += 1
print(i)