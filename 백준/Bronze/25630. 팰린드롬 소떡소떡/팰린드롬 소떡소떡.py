N = int(input())
a = input()
cnt = 0
for i in range(N // 2):
    if a[i] != a[N - 1 - i]:
        cnt += 1
print(cnt)