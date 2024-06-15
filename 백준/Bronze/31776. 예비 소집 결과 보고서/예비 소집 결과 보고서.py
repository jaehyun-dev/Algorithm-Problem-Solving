N = int(input())
cnt = 0
for _ in range(N):
    T = list(map(int, input().split()))
    flag = 1
    if set(T) == {-1}:
        flag = 0
    else:
        prev = T[0]
        for i in range(2):
            cur = T[i + 1]
            if (cur < prev or prev == -1) and cur != -1:
                flag = 0
                break
            prev = cur
    cnt += flag
print(cnt)