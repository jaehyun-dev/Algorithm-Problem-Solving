N = input()
ans = ''
for i in sorted(N, reverse=True):
    ans += i
print(ans)