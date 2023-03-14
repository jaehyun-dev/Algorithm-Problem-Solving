import math
N = input()
count = {}
for i in range(10):
    count[str(i)] = 0
for i in N:
    count[i] += 1
count['6'] = count['9'] = math.ceil((count['6'] + count['9']) / 2)
print(max(count.values()))