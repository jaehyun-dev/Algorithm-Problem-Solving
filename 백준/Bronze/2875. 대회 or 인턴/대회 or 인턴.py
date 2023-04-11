import math
N, M, K = map(int, input().split())
surp_N = max(0, N - 2 * M)
surp_M = max(0, M - N // 2)
K -= max(surp_N, surp_M)
print(min(N // 2, M) - math.ceil(K / 3) if K > 0 else min(N // 2, M))