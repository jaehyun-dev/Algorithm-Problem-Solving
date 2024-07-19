N = int(input())
l = [0] * N
for i in range(N):
    l[i] = int(input())
a, b, c = l[:3]
if 2 * b == a + c:
    print(l[-1] + (b - a))
else:
    print(l[-1] * (b // a))