import math
N, L, D = map(int, input().split())
l = N * L + 5 * (N - 1)
song = (([1] * L) + [0] * 5) * (N - 1) + [1] * L
bell = ([1] + ([0] * (D - 1)))
while len(bell) < l:
    bell += bell
t = 0
ans = 0
flag = 1
while t < l:
    if not song[t] and bell[t]:
        ans = t
        flag = 0
        break
    t += 1
if flag:
    ans = D * (math.ceil(l / D))
print(ans)