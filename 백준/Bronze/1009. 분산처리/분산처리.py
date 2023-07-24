import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    a, b = map(int, input().split())
    a = a % 10
    c = [a]
    n = a
    i = 2
    while i <= b:
        n = (n * a) % 10
        i += 1
        if n in c:
            break
        c.append(n)
    ans = c[b % len(c) - 1]
    print(10 if ans == 0 else ans)