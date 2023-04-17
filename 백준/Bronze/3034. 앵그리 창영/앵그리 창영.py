import math
N, W, H = map(int, input().split())
for _ in range(N):
    print("DA" if int(input()) <= math.sqrt(W ** 2 + H ** 2) else "NE")