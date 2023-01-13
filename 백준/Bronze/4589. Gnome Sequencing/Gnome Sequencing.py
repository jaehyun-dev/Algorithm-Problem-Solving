n = int(input())
print("Gnomes:")
for _ in range(n):
    a, b, c = map(int, input().split())
    print("Ordered" if a >= b >= c or a <= b <= c else "Unordered")