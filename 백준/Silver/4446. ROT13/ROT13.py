import sys
input = sys.stdin.readline
v = list("a i y e o u".split())
n = list("b k x z n h d c w g p v j q t s r l m f".split())
cv = list(map(lambda x:chr(ord(x) - 32), v))
cn = list(map(lambda x:chr(ord(x) - 32), n))
d = {}
for l in (v, cv):
    for i in range(6):
        d[l[i]] = l[(i - 3) % 6]
for l in (n, cn):
    for i in range(20):
        d[l[i]] = l[(i - 10) % 20]
for line in sys.stdin:
    ans = ""
    for i in line.strip():
        o = ord(i)
        if 65 <= o < 91 or 97 <= o < 123:
            ans += d[i]
        else:
            ans += i
    print(ans)