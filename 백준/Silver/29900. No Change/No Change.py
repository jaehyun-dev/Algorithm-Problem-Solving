import sys
input = sys.stdin.readline
N = int(input())
n = list(map(int, input().split()))
n.sort()
i = 1
for coin in n:
    if coin <= i:
        i += coin
    else:
        break
print(i)