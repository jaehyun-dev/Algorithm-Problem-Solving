import sys
for line in sys.stdin:
    n, k = map(int, line.strip().split())
    cnt = n
    c = n
    while k <= c:
        n = c // k
        c = c % k + n
        cnt += n
    print(cnt)