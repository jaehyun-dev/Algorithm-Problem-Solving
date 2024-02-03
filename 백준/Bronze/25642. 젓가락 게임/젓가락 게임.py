A, B = map(int, input().split())
flag = True
while A < 5 and B < 5:
    if flag:
        B += A
    else:
        A += B
    flag = not flag
print("yj" if flag else "yt")