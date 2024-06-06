a = input()
N = int(input())
ans = 0
for _ in range(N):
    b = input()
    if a[:5] == b[:5]:
        ans += 1
print(ans)