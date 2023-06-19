import sys
input = sys.stdin.readline
N = int(input())
a = {"D": 0, "P": 0}
for _ in range(N):
    b = input().strip()
    a[b] += 1
    if a["D"] - a["P"] > 1 or a["D"] - a["P"] < -1:
        break
print(f"{a['D']}:{a['P']}")