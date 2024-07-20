N, C = map(int, input().split())
check = [0] * (C + 1)
for _ in range(N):
    p = int(input())
    for i in range(1, (C // p) + 1):
        check[p * i] = 1
print(sum(check))