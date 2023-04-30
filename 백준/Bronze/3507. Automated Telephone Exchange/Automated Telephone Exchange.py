n = int(input())
count = 0
for i in range(100):
    for j in range(100):
        if n - i - j == 0:
            count += 1
print(count)