N = int(input())
a = list(map(int, input().split()))
ans = 0
for i in range(N):
    cnt = a[i] - (N - i)
    if ans < cnt:
        ans = cnt
print(ans)