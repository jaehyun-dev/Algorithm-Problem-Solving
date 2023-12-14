N = int(input())
a = []
for _ in range(N):
    a.append(input())
cnt = 0
for i in range(N):
    if a[i] == input():
        cnt += 1
print(cnt)