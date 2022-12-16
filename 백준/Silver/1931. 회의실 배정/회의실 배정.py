import sys
n = int(sys.stdin.readline().strip())
arr = []
for _ in range(n):
    a, b = map(int, sys.stdin.readline().strip().split())
    arr.append([a, b])
arr.sort(key= lambda x:[x[1], x[0]])
ans = []
ans.append(arr[0])
for i in range(1, n):
    if arr[i][0] >= ans[-1][1]:
        ans.append(arr[i])
print(len(ans))