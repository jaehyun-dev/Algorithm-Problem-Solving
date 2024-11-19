n = int(input())
x = list(map(int, input().split()))
c = 0
for i in range(n - 1):
    for j in range(i + 1, n):
        c += abs(x[i] - x[j])
print(c * 2)