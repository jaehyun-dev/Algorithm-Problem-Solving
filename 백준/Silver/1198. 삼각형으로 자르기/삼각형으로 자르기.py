n = int(input())
arr = []
max_area = 0
for _ in range(n):
    arr.append(list(map(int, input().split())))

for i in range(0, n -2):
    for j in range(i + 1, n - 1):
        for k in range(j + 1, n):
            x = [arr[i][0], arr[j][0], arr[k][0]]
            y = [arr[i][1], arr[j][1], arr[k][1]]
            area = abs(1/2 * ((x[0]*(y[1]-y[2])) + (x[1]*(y[2]-y[0])) + (x[2]*(y[0]-y[1]))))
            if area > max_area:
                max_area = area

print(max_area)