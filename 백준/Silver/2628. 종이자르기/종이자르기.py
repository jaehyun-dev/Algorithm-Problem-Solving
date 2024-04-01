W, H = map(int, input().split())
n = int(input())
r = [H]
c = [W]
for _ in range(n):
    d, i = map(int, input().split())
    if d:
        c.append(i)
    else:
        r.append(i)
r.sort()
c.sort()
s = 0
pr = 0
for i in r:
    pc = 0
    for j in c:
        if s < (i - pr) * (j - pc):
            s = (i - pr) * (j - pc)
        pc = j
    pr = i
print(s)