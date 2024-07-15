N = int(input())
l = [0] * N
for i in range(N):
    l[i] = int(input())
H = l[0]
cnt = 1
for i in range(1, N):
    if H < l[i]:
        H = l[i]
        cnt += 1
print(cnt)
H = l[-1]
cnt = 1
for i in range(N - 2, -1, -1):
    if H < l[i]:
        H = l[i]
        cnt += 1
print(cnt)