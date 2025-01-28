N, A, B = map(int, input().split())
a = b = 1
for _ in range(N):
    a += A
    b += B
    if a < b:
        a, b = b, a
    elif a == b:
        b -= 1
print(a, b)