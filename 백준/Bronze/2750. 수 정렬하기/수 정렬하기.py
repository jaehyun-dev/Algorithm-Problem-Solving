N = int(input())
l = [0] * N
for i in range(N):
    l[i] = int(input())
for i in sorted(l):
    print(i)