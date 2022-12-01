n = input().zfill(2)
m = n
count = 0
while True:
    a, b = int(m[0]), int(m[1])
    sum = str(a + b).zfill(2)
    new = str(b) + str(sum[1])
    m = new.zfill(2)
    count += 1
    if int(m) == int(n):
        break
print(count)