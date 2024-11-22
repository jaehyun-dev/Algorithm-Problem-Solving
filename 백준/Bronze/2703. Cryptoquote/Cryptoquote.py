T = int(input())
for _ in range(T):
    e = input()
    d = input()
    ans = ""
    for i in e:
        o = ord(i)
        if o == 32:
            ans += " "
        else:
            ans += d[ord(i) - 65]
    print(ans)