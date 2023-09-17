import sys
input = sys.stdin.readline
N, a, b = map(int, input().split())
l = []
flag = True
for i in range(N):
    l.append(list(map(int, input().split())))
j = l[a - 1][b - 1]
for r in range(N):
    if j < l[r][b - 1]:
        flag = False
        break
if flag:
    for c in range(N):
        if j < l[a - 1][c]:
            flag = False
            break
print("HAPPY" if flag else "ANGRY")