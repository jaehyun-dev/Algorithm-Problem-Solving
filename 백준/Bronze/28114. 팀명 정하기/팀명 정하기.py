p = []
y = []
s = {}
for _ in range(3):
    P, Y, S = input().split()
    p.append(int(P))
    y.append(int(Y))
    s[int(P)] = S
y.sort()
p.sort(reverse=True)
for i in range(3):
    print(y[i] % 100, end="")
print()
for i in range(3):
    print(s[p[i]][:1], end="")