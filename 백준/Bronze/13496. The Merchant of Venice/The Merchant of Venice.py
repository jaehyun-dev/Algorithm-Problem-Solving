k = int(input())
for i in range(k):
    n, s, d = map(int, input().split())
    a = 0
    for _ in range(n):
        d_i, v_i = map(int, input().split())
        if d_i <= s * d:
            a += v_i
    print(f"Data Set {i + 1}:")
    print(a)
    print()