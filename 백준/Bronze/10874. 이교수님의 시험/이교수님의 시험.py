N = int(input())
ans = []
for n in range(N):
    l = list(map(int, input().split()))
    flag = 1
    for i in range(10):
        if l[i] != (i % 5) + 1:
            flag = 0
            break
    if flag:
        ans.append(n + 1)
for n in ans:
    print(n)