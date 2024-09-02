while 1:
    s, d = input().split()
    if s == "00:00" and d == "00:00":
        break
    sh, sm = map(int, s.split(":"))
    dh, dm = map(int, d.split(":"))
    h = sh + dh
    m = sm + dm + h * 60
    h = m // 60
    m %= 60
    n = h // 24
    h %= 24
    ans = str(h).zfill(2) + ":" + str(m).zfill(2)
    if 0 < n:
        ans += f" +{n}"
    print(ans)