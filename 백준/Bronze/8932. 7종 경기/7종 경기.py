import sys
input = sys.stdin.readline
c = [[9.23076, 26.7, 1.835, 1], [1.84523, 75, 1.348, 0], [56.0211, 1.5, 1.05, 0], [4.99087, 42.5, 1.81, 1], [0.188807, 210, 1.41, 0], [15.9803, 3.8, 1.04, 0], [0.11193, 254, 1.88, 1]]
T = int(input())
for _ in range(T):
    a = list(map(int, input().split()))
    s = 0
    for i in range(len(a)):
        if c[i][-1]:
            s += int(c[i][0] * (c[i][1] - a[i]) ** c[i][2])
        else:
            s += int(c[i][0] * (a[i] - c[i][1]) ** c[i][2])
    print(s)