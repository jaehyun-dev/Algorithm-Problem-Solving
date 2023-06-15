g, p, t = map(int, input().split())
count = g + t * p
if g * p < count:
    print(1)
elif g * p > count:
    print(2)
else:
    print(0)