N = int(input())
p = [(209, 8), (219, 4), (229, 2), (239, 1)]
M = 0
idx = 0
for i in range(4):
    lvl = N
    for j in range(p[i][1]):
        if p[i][0] < lvl:
            break
        lvl += 1
    if M <= lvl:
        M = lvl
        idx = i
    else:
        break
print(idx + 1)