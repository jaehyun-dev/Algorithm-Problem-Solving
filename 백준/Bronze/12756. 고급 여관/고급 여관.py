a, b = map(int, input().split())
c, d = map(int, input().split())
while 1:
    b -= c
    d -= a
    if b < 1 or d < 1:
        break
if b < 1 and d < 1:
    print("DRAW")
elif b < 1:
    print("PLAYER B")
else:
    print("PLAYER A")