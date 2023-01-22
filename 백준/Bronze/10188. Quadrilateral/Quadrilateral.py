n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    for _ in range(b):
        print("X" * a)
    print()