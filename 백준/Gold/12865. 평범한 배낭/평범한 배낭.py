N, K = map(int, input().split())
knapsack = [([0] * (K + 1)) for _ in range(N + 1)]
item = [None]
for _ in range(N):
    item.append(tuple(map(int, input().split())))
for i in range(1, N + 1):
    for j in range(1, K + 1):
        knapsack[i][j] = knapsack[i - 1][j]
        if item[i][0] <= j:
            knapsack[i][j] = max(knapsack[i][j], knapsack[i - 1][j - item[i][0]] + item[i][1])
print(knapsack[N][K])