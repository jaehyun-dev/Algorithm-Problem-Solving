t = int(input())
for _ in range(t):
    n = int(input())
    l = sorted(list(map(int, input().split())))
    print((l[-1] - l[0]) * 2)