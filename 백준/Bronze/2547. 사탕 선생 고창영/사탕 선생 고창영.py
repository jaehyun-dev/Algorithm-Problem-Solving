import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    input()
    N = int(input())
    count = 0
    for _ in range(N):
        count += int(input())
    if count % N == 0:
        print("YES")
    else:
        print("NO")