A, B = map(int, input().split())
q = A // B
r = A % B
if r < 0:
    r = abs(B) + r
    q += 1
print(q, r)