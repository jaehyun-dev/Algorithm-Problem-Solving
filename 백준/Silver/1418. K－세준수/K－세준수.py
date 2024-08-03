import math
N = int(input())
K = int(input())
c = [1] * (N + 1)
for i in range(2, N + 1):
    if c[i]:
        j = 2
        while i * j <= N:
            c[i * j] = 0
            j += 1
p = []
for i in range(K + 1, N + 1):
    if c[i]:
        p.append(i)
cnt = min(N, K)
for i in range(K + 1, N + 1):
    flag = 1
    if not c[i]:
        for j in p:
            if not i % j:
                flag = 0
                break
        cnt += flag
print(cnt)