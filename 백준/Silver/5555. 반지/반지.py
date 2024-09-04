t = input()
N = int(input())
cnt = 0
for _ in range(N):
    a = input()
    a += a[:len(t) - 1]
    if t in a:
        cnt += 1
print(cnt)