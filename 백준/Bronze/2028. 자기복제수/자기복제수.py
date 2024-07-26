T = int(input())
for _ in range(T):
    N = int(input())
    s = N ** 2
    print("YES" if str(s)[-len(str(N)):] == str(N) else "NO")