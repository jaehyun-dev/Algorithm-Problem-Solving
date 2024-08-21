import sys
input = sys.stdin.readline

while 1:
    N, M = map(int, input().split())
    if (N, M) == (0, 0):
        break
    s = set()
    for _ in range(N):
        s.add(int(input()))
    cnt = 0
    for _ in range(M):
        if int(input()) in s:
            cnt += 1
    print(cnt)