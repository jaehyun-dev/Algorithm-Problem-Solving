N = int(input())
l = list(map(int, input().split()))
a = [0] * N
n = list(range(N))
for i in range(N):
    a[n[l[i]]] = i + 1
    n.pop(l[i])
print(*a)