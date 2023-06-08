T = int(input())
for _ in range(T):
    count = 0
    N, K = map(int, input().split())
    a = list(map(int, input().split()))
    for i in a:
        count += i // K
    print(count)