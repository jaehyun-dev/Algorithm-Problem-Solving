N, K = map(int, input().split())
i = 1
s = []
l = []
while i <= N ** (1 / 2):
    if N % i == 0:
        s.append(i)
        l.append(N // i)
    i += 1
if s[-1] == l[-1]:
    l.pop()
n = s + l[::-1]
try:
    print(n[K - 1])
except:
    print(0)