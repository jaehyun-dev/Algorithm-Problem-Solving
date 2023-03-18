M = 0
count = 0
for _ in range(10):
    o, i = map(int, input().split())
    count = count - o + i
    M = max(M, count)
print(M)