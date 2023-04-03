max_num = 0
row = 1
column = 1
for i in range(1, 10):
    a = list(map(int, input().split()))
    for j in range(1, 10):
        if a[j - 1] > max_num:
            max_num = a[j - 1]
            row = i
            column = j
print(max_num)
print(row, column)