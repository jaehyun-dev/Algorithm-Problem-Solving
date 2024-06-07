N = int(input())
K = input()
e = 0
o = 0
for i in K:
    if int(i) % 2 == 0:
        e += 1
    else:
        o += 1
if o < e:
    print(0)
elif e < o:
    print(1)
else:
    print(-1)