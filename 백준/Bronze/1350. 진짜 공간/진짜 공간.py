import math
N = int(input())
f = list(map(int, input().split()))
c = int(input())
cnt = 0
for s in f:
    cnt += math.ceil(s / c)
print(cnt * c)