import sys
input = sys.stdin.readline
n = int(input())
arr = [0] * 10001
for _ in range(n):
    a = int(input())
    arr[a] += 1
for i in range(10001):
#    if arr[i]:
    for _ in range(arr[i]):
        print(i)