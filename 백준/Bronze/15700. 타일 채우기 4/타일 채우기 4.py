N, M = map(int, input().split())
print(max((((N // 2) * M) + ((N % 2) * M // 2)), ((N * (M // 2)) + ((N // 2) * (M % 2)))))