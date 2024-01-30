N = int(input())
x = list(map(int, input().split()))
flag = 1
i = 0
cnt = 0
p = -1
while i < N:
    c = x[i]
    if c - p != 1:
        cnt += c
    p = c
    i += 1
print(cnt)