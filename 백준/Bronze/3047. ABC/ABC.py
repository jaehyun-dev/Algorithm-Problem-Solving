a = list(map(int, input().split()))
a.sort()
for i in input():
    print(a[ord(i) - 65], end=" ")