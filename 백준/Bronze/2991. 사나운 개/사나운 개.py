A, B, C, D = map(int, input().split())
P, M, N = map(int, input().split())
for i in [P, M, N]:
    count = 0
    if 0 < i % (A + B) <= A:
        count += 1
    if 0 < i % (C + D) <= C:
        count += 1
    print(count)