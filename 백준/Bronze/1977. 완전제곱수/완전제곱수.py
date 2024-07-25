import math
M = int(input())
N = int(input())
ans = 0
m = 0
flag = 1
for i in range(M, N + 1):
    if math.sqrt(i) == int(math.sqrt(i)):
        if flag:
            m = i
            flag = 0
        ans += i
if flag:
    print(-1)
else:
    print(ans)
    print(m)