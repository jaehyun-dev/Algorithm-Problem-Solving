N, b = map(int, input().split())
if N < 2 ** (b + 1):
    print("yes")
else:
    print("no")