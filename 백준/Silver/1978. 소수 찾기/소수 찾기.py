n = int(input())
arr = [True] * 1000
arr[0] = False
i = 0
while i < 500:
    if arr[i] == False:
        i += 1
    else:
        j = 2
        while (i + 1) * j <= 1000:
            arr[(i + 1) * j - 1] = False
            j += 1
        i += 1

num = list(map(int, input().split()))
count = 0
for i in num:
    if arr[i - 1]:
        count += 1

print(count)