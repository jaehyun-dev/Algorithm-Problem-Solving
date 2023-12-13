import sys
a = []
b = []
for line in sys.stdin:
    c, t = line.strip().split()
    a.append(c)
    b.append(int(t))
print(a[b.index(min(b))])