T = int(input())
s = list(map(int, input().split()))
for i in range(5 - T):
    s += [0]
k, m, e, t, f = s
if e < k:
    s1 = (k - e) * 508
else:
    s1 = (e - k) * 108
if t < m:
    s2 = (m - t) * 212
else:
    s2 = (t - m) * 305
if T == 5:
    s3 = f * 707
else:
    s3 = 0
print((s1 + s2 + s3) * 4763)