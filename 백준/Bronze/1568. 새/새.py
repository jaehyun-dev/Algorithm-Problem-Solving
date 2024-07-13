N = int(input())
K = 1
t = 0
while 0 < N:
    if N < K:
        K = 1
    N -= K
    K += 1
    t += 1
print(t)