import sys
input = sys.stdin.readline
n = int(input())
arr = []
dp = [int(input())]
for _ in range(1, n):
    arr = list(map(int, input().split()))
    temp = []
    for i in range(len(arr)):
        if i < 1:
            temp.append(dp[i] + arr[i])
        elif i < len(arr) - 1:
            temp.append(max(dp[i - 1] + arr[i], dp[i] + arr[i]))
        else:
            temp.append(dp[i - 1] + arr[i])
    dp = temp
print(max(dp))