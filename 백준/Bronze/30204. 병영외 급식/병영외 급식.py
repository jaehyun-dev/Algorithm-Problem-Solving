N, X = map(int, input().split())
p = list(map(int, input().split()))
print(1 if sum(p) % X == 0 else 0)