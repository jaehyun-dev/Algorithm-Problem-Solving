import sys
input = sys.stdin.readline
N = int(input())
ones = [0] * 20
for _ in range(N):
    a = int(input())
    b = bin(a)[2:].zfill(20)
    for i in range(20):
        if b[i] == '1':
            ones[i] += 1
ans = 0
for i in range(20):
    ans += (ones[i] * (N - ones[i])) * (2 ** (19 - i))

print(ans)