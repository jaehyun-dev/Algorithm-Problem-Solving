import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    p1 = 0
    p2 = 0
    for _ in range(n):
        a, b = input().split()
        if a == 'R' and b == 'P':
            p2 += 1
        elif a == 'P' and b == 'R':
            p1 += 1
        elif a == 'P' and b == 'S':
            p2 += 1
        elif a == 'S' and b == 'P':
            p1 += 1
        elif a == 'S' and b == 'R':
            p2 += 1
        elif a == 'R' and b == 'S':
            p1 += 1
    if p1 > p2:
        print('Player 1')
    elif p1 < p2:
        print('Player 2')
    else:
        print('TIE')