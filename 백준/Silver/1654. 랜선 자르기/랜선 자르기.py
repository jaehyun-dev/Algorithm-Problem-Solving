import sys
input = sys.stdin.readline
k, n = map(int, input().split())
arr = []
for _ in range(k):
    arr.append(int(input()))

start = 1
end = max(arr)
while start <= end:
    index = (start + end) // 2
    count = 0
    while count < n:
        for i in range(len(arr)):
            count += arr[i] // index
        if i == len(arr) - 1:
            break
    if count < n:
        end = index - 1
    else:
        start = index + 1

print(end)