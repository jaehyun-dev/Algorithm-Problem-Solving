ans = 0
b = 0
for i in range(3):
    p, w = map(int, input().split())
    tp = p * 10
    if 5000 <= tp:
        tp -= 500
    tw = w * 10
    r = tw / tp
    if b < r:
        b = r
        ans = i
print("SNU"[ans])