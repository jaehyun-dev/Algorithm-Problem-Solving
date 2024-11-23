T = int(input())
for _ in range(T):
    l = input().split()
    i = int(l[0])
    s = l[1]
    ans = s[:i - 1] + s[i:]
    print(ans)