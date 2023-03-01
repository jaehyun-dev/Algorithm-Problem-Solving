X = int(input())
count = 0
i = 0
prev = 0
mod = 1
while count < X:
    i += 1
    count += i
    mod *= -1
    if count >= X:
        break
    prev = count
if mod == 1:
    print(f"{[*range(1, i + 1)][X - prev - 1]}/{[*range(i, 0, -1)][X - prev - 1]}")
else:
    print(f"{[*range(i, 0, -1)][X - prev - 1]}/{[*range(1, i + 1)][X - prev - 1]}")