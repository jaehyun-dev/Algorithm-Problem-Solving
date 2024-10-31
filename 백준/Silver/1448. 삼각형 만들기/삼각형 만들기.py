import sys
input = sys.stdin.readline
N = int(input())
l = [0] * N
for i in range(N):
    l[i] = int(input())
l.sort(reverse=True)
ans = -1
for i in range(N - 2):
    flag = 1
    for j in range(i + 1, N - 1):
        flag = 1
        for k in range(j + 1, N):
            if l[j] + l[k] <= l[i]:
                flag = 0
            else:
                ans = l[j] + l[k] + l[i]
                flag = 1
            break
        if flag:
            break
    if flag:
        break
print(ans)