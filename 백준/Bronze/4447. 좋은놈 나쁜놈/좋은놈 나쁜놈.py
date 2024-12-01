import sys
input = sys.stdin.readline
n = int(input())
for _ in range(n):
    h = input().strip()
    d = {'B': 0, 'b': 0, 'G': 0, 'g': 0}
    for i in h:
        if i in d:
            d[i] += 1
    ans = "NEUTRAL"
    if d['B'] + d['b'] < d['G'] + d['g']:
        ans = "GOOD"
    elif d['G'] + d['g'] < d['B'] + d['b']:
        ans = "A BADDY"
    print(f"{h} is {ans}")