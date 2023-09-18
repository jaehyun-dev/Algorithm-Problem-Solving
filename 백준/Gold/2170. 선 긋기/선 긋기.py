import sys
input = sys.stdin.readline
N = int(input())
l = []
for _ in range(N):
    x, y = map(int, input().split())
    l.append((x, y))
l.sort()
c = 0
s = l[0][0]
e = l[0][1]
for i in range(1, N):
    if l[i][0] <= e:
        if l[i][1] >= e:
            e = l[i][1]
        else:
            continue
    else:
        c += e - s
        s = l[i][0]
        e = l[i][1]
c += e - s
print(c)