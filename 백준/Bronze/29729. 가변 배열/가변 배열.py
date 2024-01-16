import sys
input = sys.stdin.readline
S, N, M = map(int, input().split())
cnt = 0
for _ in range(N + M):
    if int(input()):
        if cnt == S:
            S *= 2
        cnt += 1
    else:
        cnt -= 1
print(S)