import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N = int(input())
    cnt = 0
    for b in range(2, N // 2 + 1):
        n = N
        while 0 < n:
            if n % b == 0:
                cnt += 1
                n //= b
            else:
                break
    if N != 1:
        cnt += 1
    print(cnt)