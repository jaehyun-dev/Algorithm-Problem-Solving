import sys
input = sys.stdin.readline
Q = int(input())
for _ in range(Q):
    a = int(input())
    print(int(a == a & (-a)))