T = int(input())
for _ in range(T):
    n, l = input().split()
    a = ord(l)
    for i in range(1, int(n) + 1):
        if a == 91:
            a = 65
        print(chr(a) * i)
        a += 1
    print()