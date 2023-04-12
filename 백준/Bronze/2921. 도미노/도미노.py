N = int(input())
count = 0
for i in range(N + 1):
    for j in range(i, N + 1):
        count += i + j
print(count)