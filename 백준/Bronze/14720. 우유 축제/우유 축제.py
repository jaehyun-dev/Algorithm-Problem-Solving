N = int(input())
a = list(map(int, input().split()))
b = 0
c = 0
for i in range(N):
    if a[i] == b % 3:
        c += 1
        b += 1
print(c)