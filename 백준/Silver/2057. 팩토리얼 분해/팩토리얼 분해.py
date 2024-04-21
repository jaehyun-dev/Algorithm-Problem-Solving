import math
import itertools

N = int(input())
a = []
i = 0
while 1:
    f = math.factorial(i)
    if N < f:
        break
    a.append(math.factorial(i))
    i += 1
flag = 0
for i in range(1, len(a) + 1):
    for c in itertools.combinations(a, i):
        if sum(c) == N:
            print("YES")
            flag = 1
            break
    if flag:
        break
if not flag:
    print("NO")