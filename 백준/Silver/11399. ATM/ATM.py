n = int(input())
arr = list(map(int, input().split()))
arr.sort()
count = 0
for i in range(n):
    count += arr[i] * (n - i)
print(count)