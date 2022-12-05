import sys
n = int(input())
for _ in range(n):
    H, W, N = map(int, sys.stdin.readline().strip().split())
    floor = H if N % H == 0 else N % H
    unit = N // H + 1 if N % H != 0 else N // H
    print(str(floor)+str(unit).zfill(2))