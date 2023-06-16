n, d = map(int, input().split())
count = []
for _ in range(n):
    count.append(int(input()))
cash = d // sum(count)
for i in range(n):
    print(count[i] * cash)