import math
M = int(input())
N = int(input())
p = [1] * (N + 1)
for i in range(2, int(math.sqrt(N)) + 1):
    if p[i]:
        j = 2
        while i * j <= N:
            p[i * j] = 0
            j += 1
p[0] = p[1] = 0
s = 0
flag = 1
for i in range(M, N + 1):
    if p[i]:
        s += i
        if flag:
            m = i
            flag = 0
if flag:
    print(-1)
else:
    print(s)
    print(m)