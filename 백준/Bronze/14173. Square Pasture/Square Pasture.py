x11, y11, x12, y12 = map(int, input().split())
x21, y21, x22, y22 = map(int, input().split())
x31 = min(x11, x21)
y31 = min(y11, y21)
x32 = max(x12, x22)
y32 = max(y12, y22)
print(max(x32 - x31, y32 - y31) ** 2)