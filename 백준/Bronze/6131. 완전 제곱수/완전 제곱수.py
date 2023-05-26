N = int(input())
count = 0
for i in range(1, 501):
    for j in range(i, 501):
        if i ** 2 + N == j ** 2:
            count += 1
print(count)