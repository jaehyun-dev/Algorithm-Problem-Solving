import sys
input = sys.stdin.readline

N = int(input())
for _ in range(N):
    n = input()
    if 'S' in n:
        print(n)
        break