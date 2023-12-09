T = int(input())
for _ in range(T):
    n = int(input())
    q = n // 5
    r = n % 5
    print("++++ " * q + "|" * r)