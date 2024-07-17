N, L = map(int, input().split())
cnt = 0
i = 0
while cnt < N:
    i += 1
    if str(L) not in str(i):
        cnt += 1
print(i)