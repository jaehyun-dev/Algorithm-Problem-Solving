N = int(input())
l = sorted(list(map(int, input().split())))
m = 0
for i in range(N - 1):
    m += abs(l[i] - l[i + 1])
m += abs(l[0] - l[-1])
print(m)