import sys
input = sys.stdin.readline
N, B, H, W = map(int, input().split())
m = B + 1
for _ in range(H):
    p = int(input())
    l = list(map(int, input().split()))
    c = B + 1
    for i in l:
        if N <= i:
            c = N * p
            break
    if c < m and c <= B:
        m = c
print(m if m <= B else "stay home")