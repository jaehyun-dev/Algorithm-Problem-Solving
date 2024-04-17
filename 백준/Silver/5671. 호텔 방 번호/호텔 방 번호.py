import sys
for line in sys.stdin:
    N, M = map(int, line.split())
    cnt = 0
    for i in range(N, M + 1):
        l = len(str(i))
        s = set()
        while 0 < i:
            s.add(i % 10)
            i //= 10
        if len(s) == l:
           cnt += 1
    print(cnt)