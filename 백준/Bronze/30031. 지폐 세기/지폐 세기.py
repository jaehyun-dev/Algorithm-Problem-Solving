import sys
input = sys.stdin.readline
N = int(input())
m = {136: 1000,
     142: 5000,
     148: 10000,
     154: 50000}
cnt = 0
for _ in range(N):
    cnt += m[list(map(int, input().split()))[0]]
print(cnt)