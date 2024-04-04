import sys
input = sys.stdin.readline
N, K = map(int, input().split())
a = []
for _ in range(N):
    a.append(float(input()))
a.sort()
if not K:
    ans1 = format(sum(a) / N, ".2f")
    ans2 = ans1
else:
    a = [a[K]] * K + a[K:N - K] + [a[N - K - 1]] * K
    ans1 = format(sum(a[K:N - K]) / (N - 2 * K) + 1e-6, ".2f")
    ans2 = format(sum(a) / N + 1e-6, ".2f")
print(ans1)
print(ans2)