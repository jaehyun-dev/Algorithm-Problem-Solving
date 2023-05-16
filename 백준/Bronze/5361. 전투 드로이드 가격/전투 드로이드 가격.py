a = [350.34, 230.90, 190.55, 125.30, 180.90]
T = int(input())
for _ in range(T):
    b = list(map(int, input().split()))
    print(f"${format(sum(map(lambda x, y: x * y, a, b)), '.2f')}")