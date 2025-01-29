N = int(input())
l = list(map(int, input().split()))
r = 0
for i in range(N):
    if l[i]:
        r += 1
    else:
        r -= 1
    l[i] = r
print(sum(l))