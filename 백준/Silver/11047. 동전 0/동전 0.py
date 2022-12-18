import sys
n, k = map(int, sys.stdin.readline().strip().split())
arr = []
for _ in range(n):
    arr.append(int(sys.stdin.readline().strip()))

count = 0
while k > 0:
    for i in range(len(arr) - 1, 0, -1):
        if arr[i] > k:
            arr.pop()
        else:
            break
    share = k // arr[-1]
    count += share
    k -= share * arr[-1]

print(count)