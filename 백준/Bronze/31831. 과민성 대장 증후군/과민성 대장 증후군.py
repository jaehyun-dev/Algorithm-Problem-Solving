N, M = map(int, input().split())
A = list(map(int, input().split()))
s, c = 0, 0
for a in A:
    if 0 <= a + s:
        s += a
    else:
        s = 0
    if M <= s:
        c += 1
print(c)