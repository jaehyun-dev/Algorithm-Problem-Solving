import itertools
y = input()
a = {}
for i in "LOVE":
    a[i] = y.count(i)
b = dict(a)
N = int(input())
M = 0
n = []
for _ in range(N):
    a = dict(b)
    t = input()
    for i in "LOVE":
        a[i] += t.count(i)
    p = 1
    for case in itertools.combinations(list("LOVE"), 2):
        p *= (a[case[0]] + a[case[1]])
    p %= 100
    if M < p:
        n = [t]
        M = p
    elif M == p:
        n.append(t)
n.sort()
print(n[0])