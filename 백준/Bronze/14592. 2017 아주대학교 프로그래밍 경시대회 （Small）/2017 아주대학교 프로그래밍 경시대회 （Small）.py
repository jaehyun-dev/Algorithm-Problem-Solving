N = int(input())
a = [0, 0, 0, 0]
for i in range(1, N + 1):
    S, C, L = map(int, input().split())
    if S > a[0]:
        a[0] = S
        a[1] = C
        a[2] = L
        a[3] = i
    elif S == a[0] and C < a[1]:
        a[1] = C
        a[2] = L
        a[3] = i
    elif S == a[0] and C == a[1] and L < a[2]:
        a[2] = L
        a[3] = i
print(a[3])