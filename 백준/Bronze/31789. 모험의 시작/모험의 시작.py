N = int(input())
X, S = map(int, input().split())
flag = 0
for _ in range(N):
    c, p = map(int, input().split())
    if c <= X and S < p:
        flag = 1
        break
print("YES" if flag else "NO")