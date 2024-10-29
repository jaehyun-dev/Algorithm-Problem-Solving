from itertools import permutations as p
from itertools import combinations as c
K5 = input().split()
S = set()
for i in p(K5, 5):
    num = ""
    for s in i:
        num += s
    if num[0] == '0':
        continue
    else:
        S.add(int(num))
cnt = 0
for i in c(S, 4):
    l = sorted(i)
    if sum(l[:3]) == l[3]:
        cnt += 1
print(cnt)