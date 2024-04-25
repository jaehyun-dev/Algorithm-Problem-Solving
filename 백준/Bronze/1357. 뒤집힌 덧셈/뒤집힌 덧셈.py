def rev(x):
    return int(str(x)[::-1])

X, Y = map(int, input().split())
print(rev(rev(X) + rev(Y)))