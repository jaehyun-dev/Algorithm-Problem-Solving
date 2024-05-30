T = int(input())
for _ in range(T):
    h, w = map(int, input().split())
    b = w / ((h /100) ** 2)
    if h < 140.1:
        print(6)
    elif h < 146:
        print(5)
    elif h < 159:
        print(4)
    elif h < 161:
        if 16 <= b < 35:
            print(3)
        else:
            print(4)
    elif h < 204:
        if 20 <= b < 25:
            print(1)
        elif 18.5 <= b < 20 or 25 <= b < 30:
            print(2)
        elif 16 <= b < 18.5 or 30 <= b < 35:
            print(3)
        else:
            print(4)
    else:
        print(4)