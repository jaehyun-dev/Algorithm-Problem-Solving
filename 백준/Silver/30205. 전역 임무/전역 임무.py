N, M, P = map(int, input().split())
outer_flag = False
for _ in range(N):
    s = list(map(int, input().split()))
    i = 0
    while i < len(s):
        s.sort()
        flag = True
        for j in range(len(s)):
            if 0 <= s[j] <= P:
                P += s[j]
                s.remove(s[j])
                flag = False
                break
        if flag:
            if s[0] == -1:
                P *= 2
                s.remove(s[0])
                continue
        if flag:
            outer_flag = True
            break
    if outer_flag:
        print(0)
        break
if not outer_flag:
    print(1)