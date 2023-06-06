T = int(input())
for _ in range(T):
    count = 0
    N, D = map(int, input().split())
    for _ in range(N):
        v, f, c = map(int, input().split())
        if D <= v * (f / c):
            count += 1
    print(count)