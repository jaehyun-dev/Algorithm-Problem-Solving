import sys
d = {}
M = 0
for line in sys.stdin:
    l = line.strip()
    for c in l:
        if c != " ":
            if c in d:
                d[c] += 1
            else:
                d[c] = 1
            if M < d[c]:
                M = d[c]
l = []
for c in d:
    if d[c] == M:
        l.append(c)
l.sort()
for c in l:
    print(c, end="")