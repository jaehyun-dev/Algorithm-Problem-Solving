import sys
input = sys.stdin.readline
n, m, b = map(int, input().split())
arr = []
num = []
for _ in range(n):
    temp = list(map(int, input().split()))
    arr.append(temp)
    num.extend(temp)

floor = sum(num) // (n * m)
# floor_ceil = floor_floor + 1

work = [[0 for _ in range(m)] for _ in range(n)]

result = []
flag = True
while flag:
    time = 0
    inventory = b
    flag = True
    for i in range(n):
        for j in range(m):
            work[i][j] = arr[i][j] - floor
            if work[i][j] >= 0:
                time += 2 * work[i][j]
                inventory += work[i][j]
            else:
                time -= work[i][j]
                inventory += work[i][j]
    if inventory < 0:
        flag = False
    if len(result) > 0 and time > result[-1][0]:
        flag = False
    if flag:
        result.append([time, floor])
    floor += 1

result.sort(key= lambda x:[x[0], -x[1]])
print(f"{result[0][0]} {result[0][1]}")