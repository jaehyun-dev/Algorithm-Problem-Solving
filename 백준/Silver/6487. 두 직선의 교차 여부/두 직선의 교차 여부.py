N = int(input())
for _ in range(N):
    x1, y1, x2, y2, x3, y3, x4, y4 = map(int, input().split())
    if x1 == x2:
        a = None
        c = None
    elif y1 == y2:
        a = 0
        c = y1
    else:
        a = (y2 - y1) / (x2 - x1)
        c = y1 - a * x1
    if x3 == x4:
        b = None
        d = None
    elif y3 == y4:
        b = 0
        d = y3
    else:
        b = (y4 - y3) / (x4 - x3)
        d = y3 - b * x3
    if a == None:
        if b == None:
            if x1 == x3:
                print("LINE")
            else:
                print("NONE")
        elif b == 0:
            print("POINT", format(x1, '.2f'), format(y3, '.2f'))
        else:
            print("POINT", format(x1, '.2f'), format(c * x1 + d, '.2f'))
    elif a == 0:
        if b == None:
            print("POINT", format(x3, '.2f'), format(y1, '.2f'))
        elif b == 0:
            if y1 == y3:
                print("LINE")
            else:
                print("NONE")
        else:
            print("POINT", format((y1 - d) / c, '.2f'), format(y1, '.2f'))
    else:
        if b == None:
            print("POINT", format(x3, '.2f'), format(a * x3 + b, '.2f'))
        elif b == 0:
            print("POINT", format((y3 - b) / a, '.2f'), format(y3, '.2f'))
        else:
            if a != b:
                print("POINT", format((d - c) / (a - b), '.2f'), format((d - c) / (a - b) * a + c, '.2f'))
            elif a == b and c == d:
                print("LINE")
            else:
                print("NONE")