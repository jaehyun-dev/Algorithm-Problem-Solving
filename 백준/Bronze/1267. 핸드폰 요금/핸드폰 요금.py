N = int(input())
a = list(map(int, input().split()))
Y = 0
M = 0
for i in range(N):
    Y += (a[i] // 30 + 1) * 10
    M += (a[i] // 60 + 1) * 15
if Y <= M:
    print("Y", end=" ")
if Y >= M:
    print("M", end=" ")
print(min(Y, M))