n = int(input())
x = sorted(list(map(int, input().split())))
c = 0
for i in range(n):
    c += x[i] * i
    c -= x[i] * (n - i - 1)
print(c * 2)