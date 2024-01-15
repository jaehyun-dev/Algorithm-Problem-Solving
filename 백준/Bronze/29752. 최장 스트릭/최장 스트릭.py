N = int(input())
s = list(map(int, input().split()))
l = 0
cnt = 0
for i in range(N):
    if s[i] == 0:
        if l < cnt:
            l = cnt
        cnt = 0
    else:
        cnt += 1
if l < cnt:
    l = cnt
print(l)