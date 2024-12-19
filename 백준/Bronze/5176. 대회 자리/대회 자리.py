K = int(input())
for _ in range(K):
    P, M = map(int, input().split())
    s = set()
    ans = 0
    for p in range(P):
        m = int(input())
        if m in s:
            ans += 1
        else:
            s.add(m)
    print(ans)