import math
N = int(input())
v = list(map(int, input().split()))
ans = 0
if math.ceil(N / 2) <= v.count(0):
    ans = "INVALID"
elif v.count(-1) < v.count(1):
    ans = "APPROVED"
else:
    ans = "REJECTED"
print(ans)