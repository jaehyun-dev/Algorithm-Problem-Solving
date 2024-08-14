import sys
for line in sys.stdin:
    l = list(map(int, line.split()))
    n, l = l[0], l[1:]
    m = [0] * (n - 1)
    for i in range(n - 1):
        m[i] = abs(l[i] - l[i + 1])
    m.sort()
    if m == list(range(1, n)):
        print("Jolly")
    else:
        print("Not jolly")