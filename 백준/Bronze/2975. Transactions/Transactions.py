import sys
input = sys.stdin.readline
while True:
    s, l, a = input().split()
    if s == '0' and l == 'W' and a == '0':
        break
    if l == 'W':
        n = int(s) - int(a)
        if n < -200:
            print("Not allowed")
        else:
            print(n)
    else:
        print(int(s) + int(a))
        