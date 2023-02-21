N = int(input())
P = int(input())

def c1(price):
    return price - 500

def c2(price):
    return int(price * 0.9)

def c3(price):
    return price - 2000

def c4(price):
    return int(price * 0.75)

ans = P

if N > 4:
    ans = min(ans, c1(P))
if N > 9:
    ans = min(ans, c2(P))
if N > 14:
    ans = min(ans, c3(P))
if N > 19:
    ans = min(ans, c4(P))

print(ans if ans > 0 else 0)