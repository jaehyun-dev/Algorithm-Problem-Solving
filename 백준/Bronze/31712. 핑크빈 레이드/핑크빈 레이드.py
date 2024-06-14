C = []
D = []
for _ in range(3):
    c, d = map(int, input().split())
    C.append(c)
    D.append(d)
H = int(input())
t = 0
while 1:
    for i in range(3):
        if not (t % C[i]):
            H -= D[i]
    if H <= 0:
        break
    t += 1
print(t)