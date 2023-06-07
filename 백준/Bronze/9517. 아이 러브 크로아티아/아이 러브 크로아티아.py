K = int(input())
N = int(input())
count = 0
for _ in range(N):
    a = list(input().split())
    T = int(a[0])
    Z = a[1]
    count += T
    if count >= 210:
        print(K % 8 if K % 8 != 0 else 8)
        break
    if Z == 'T':
        K += 1