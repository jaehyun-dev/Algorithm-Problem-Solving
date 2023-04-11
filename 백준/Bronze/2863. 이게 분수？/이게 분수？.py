n = []
for _ in range(2):
    n += map(int, input().split())
count = [0]
num = n[0] / n[2] + n[1] / n[3]
for i in range(3):
    n[0], n[1], n[2], n[3] = n[2], n[0], n[3], n[1]
    cur = n[0] / n[2] + n[1] / n[3]
    if cur > num:
        count.clear()
        count.append(i + 1)
        num = cur
    elif cur == num:
        count.append(i + 1)
print(count[0] if len(count) == 1 else num)